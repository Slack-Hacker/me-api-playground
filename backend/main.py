from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from typing import List, Optional
from database import get_session, create_db_and_tables
from models import Profile, Skill, Project, Education, WorkExperience, Link, ProjectLink

app = FastAPI(
    title="Me-API Playground",
    description="Personal profile API for candidate information",
    version="1.0.0"
)

import os

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    os.getenv("FRONTEND_URL", "")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from seed import seed_database
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    seed_database()


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running"}


@app.get("/api/profile")
def get_profile(session: Session = Depends(get_session)):
    """Get complete profile with all related data"""
    profile = session.exec(select(Profile)).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    # Manually construct response with relationships
    return {
        "id": profile.id,
        "name": profile.name,
        "email": profile.email,
        "bio": profile.bio,
        "location": profile.location,
        "skills": [{"id": s.id, "name": s.name} for s in profile.skills],
        "projects": [
            {
                "id": p.id,
                "title": p.title,
                "description": p.description,
                "technologies": p.technologies.split(","),
                "links": [{"platform": l.platform, "url": l.url} for l in p.links]
            }
            for p in profile.projects
        ],
        "education": [
            {
                "id": e.id,
                "institution": e.institution,
                "degree": e.degree,
                "field_of_study": e.field_of_study,
                "start_date": e.start_date,
                "end_date": e.end_date
            }
            for e in profile.education
        ],
        "work": [
            {
                "id": w.id,
                "company": w.company,
                "position": w.position,
                "description": w.description,
                "start_date": w.start_date,
                "end_date": w.end_date
            }
            for w in profile.work
        ],
        "links": [{"platform": l.platform, "url": l.url} for l in profile.links]
    }


@app.put("/api/profile")
def update_profile(
    name: Optional[str] = None,
    email: Optional[str] = None,
    bio: Optional[str] = None,
    location: Optional[str] = None,
    session: Session = Depends(get_session)
):
    """Update profile information"""
    profile = session.exec(select(Profile)).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    if name:
        profile.name = name
    if email:
        profile.email = email
    if bio:
        profile.bio = bio
    if location:
        profile.location = location
    
    session.add(profile)
    session.commit()
    session.refresh(profile)
    
    return {"message": "Profile updated successfully", "profile": profile}


@app.get("/api/projects")
def get_projects(
    skill: Optional[str] = Query(None, description="Filter projects by skill/technology"),
    session: Session = Depends(get_session)
):
    """Get all projects, optionally filtered by skill"""
    profile = session.exec(select(Profile)).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    projects = profile.projects
    
    # Filter by skill if provided
    if skill:
        skill_lower = skill.lower()
        projects = [
            p for p in projects
            if any(tech.strip().lower() == skill_lower for tech in p.technologies.split(","))
        ]
    
    return {
        "projects": [
            {
                "id": p.id,
                "title": p.title,
                "description": p.description,
                "technologies": p.technologies.split(","),
                "links": [{"platform": l.platform, "url": l.url} for l in p.links]
            }
            for p in projects
        ]
    }


@app.get("/api/skills/top")
def get_top_skills(
    limit: int = Query(10, description="Number of skills to return"),
    session: Session = Depends(get_session)
):
    """Get top skills"""
    skills = session.exec(select(Skill).limit(limit)).all()
    return {"skills": [{"id": s.id, "name": s.name} for s in skills]}


@app.get("/api/search")
def search(
    q: str = Query(..., description="Search query"),
    session: Session = Depends(get_session)
):
    """Search across projects, skills, and profile"""
    profile = session.exec(select(Profile)).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    query_lower = q.lower()
    
    # Search in projects
    matching_projects = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "technologies": p.technologies.split(","),
            "links": [{"platform": l.platform, "url": l.url} for l in p.links]
        }
        for p in profile.projects
        if query_lower in p.title.lower() 
        or query_lower in p.description.lower()
        or query_lower in p.technologies.lower()
    ]
    
    # Search in skills
    matching_skills = [
        {"id": s.id, "name": s.name}
        for s in profile.skills
        if query_lower in s.name.lower()
    ]
    
    return {
        "query": q,
        "results": {
            "projects": matching_projects,
            "skills": matching_skills
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
