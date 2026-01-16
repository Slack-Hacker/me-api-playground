from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class Skill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    profile_id: Optional[int] = Field(default=None, foreign_key="profile.id")
    profile: Optional["Profile"] = Relationship(back_populates="skills")


class Link(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    platform: str  # github, linkedin, portfolio
    url: str
    profile_id: Optional[int] = Field(default=None, foreign_key="profile.id")
    profile: Optional["Profile"] = Relationship(back_populates="links")


class Education(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    institution: str
    degree: str
    field_of_study: str
    start_date: str
    end_date: Optional[str] = None
    profile_id: Optional[int] = Field(default=None, foreign_key="profile.id")
    profile: Optional["Profile"] = Relationship(back_populates="education")


class WorkExperience(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company: str
    position: str
    description: str
    start_date: str
    end_date: Optional[str] = None
    profile_id: Optional[int] = Field(default=None, foreign_key="profile.id")
    profile: Optional["Profile"] = Relationship(back_populates="work")


class ProjectLink(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    platform: str  # github, demo, docs
    url: str
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    project: Optional["Project"] = Relationship(back_populates="links")


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str
    technologies: str  # comma-separated for simplicity
    profile_id: Optional[int] = Field(default=None, foreign_key="profile.id")
    profile: Optional["Profile"] = Relationship(back_populates="projects")
    links: List["ProjectLink"] = Relationship(back_populates="project")


class Profile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    bio: Optional[str] = None
    location: Optional[str] = None
    
    # Relationships
    skills: List["Skill"] = Relationship(back_populates="profile")
    projects: List["Project"] = Relationship(back_populates="profile")
    education: List["Education"] = Relationship(back_populates="profile")
    work: List["WorkExperience"] = Relationship(back_populates="profile")
    links: List["Link"] = Relationship(back_populates="profile")
