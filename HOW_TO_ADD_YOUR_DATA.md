# 📝 How to Add Your Personal Details

Follow these steps to replace the sample data with your own information:

## Step 1: Edit the Seed File

Open `backend/seed.py` and modify the following sections:

### 1️⃣ **Your Profile Information** (Lines 18-23)

```python
profile = Profile(
    name="Your Full Name",                    # ← Change this
    email="your.email@example.com",           # ← Change this
    bio="Your professional bio here...",      # ← Change this
    location="Your City, Country"             # ← Change this
)
```

**Example:**
```python
profile = Profile(
    name="Jane Smith",
    email="jane.smith@gmail.com",
    bio="Software engineer specializing in AI and machine learning with 5 years of experience",
    location="New York, NY"
)
```

---

### 2️⃣ **Your Skills** (Line 29)

```python
skills_data = ["Python", "FastAPI", "React", "TypeScript", "SQL", "Docker", "AWS", "Git"]
```

**Replace with your skills:**
```python
skills_data = ["JavaScript", "Node.js", "MongoDB", "Express", "Vue.js", "GraphQL", "Docker", "Kubernetes"]
```

---

### 3️⃣ **Your Education** (Lines 35-42)

```python
education = Education(
    institution="Your University Name",
    degree="Your Degree",
    field_of_study="Your Major",
    start_date="YYYY-MM",
    end_date="YYYY-MM",  # or None if still studying
    profile_id=profile.id
)
```

**Example:**
```python
education = Education(
    institution="MIT",
    degree="Master of Science",
    field_of_study="Artificial Intelligence",
    start_date="2018-09",
    end_date="2020-06",
    profile_id=profile.id
)
```

**💡 Tip:** You can add multiple education entries by creating `education1`, `education2`, etc.

---

### 4️⃣ **Your Work Experience** (Lines 46-63)

```python
work1 = WorkExperience(
    company="Your Company Name",
    position="Your Job Title",
    description="What you did at this job",
    start_date="YYYY-MM",
    end_date=None,  # None if current job, or "YYYY-MM" if past
    profile_id=profile.id
)
```

**Example:**
```python
work1 = WorkExperience(
    company="Google",
    position="Senior Software Engineer",
    description="Developed scalable microservices handling 1M+ requests/day",
    start_date="2022-01",
    end_date=None,  # Current job
    profile_id=profile.id
)

work2 = WorkExperience(
    company="Amazon",
    position="Software Development Engineer",
    description="Built AWS Lambda functions and API Gateway integrations",
    start_date="2020-06",
    end_date="2021-12",
    profile_id=profile.id
)
```

---

### 5️⃣ **Your Projects** (Lines 66-121)

```python
project1 = Project(
    title="Your Project Name",
    description="What the project does",
    technologies="Tech1,Tech2,Tech3",  # Comma-separated, no spaces
    profile_id=profile.id
)
```

**Example:**
```python
project1 = Project(
    title="AI Chatbot Platform",
    description="Built an AI-powered chatbot using GPT-4 API with custom training data",
    technologies="Python,OpenAI,FastAPI,React,PostgreSQL",
    profile_id=profile.id
)
```

**Adding Project Links:**
```python
project1_link1 = ProjectLink(
    platform="github",
    url="https://github.com/yourname/your-project",
    project_id=project1.id
)
project1_link2 = ProjectLink(
    platform="demo",
    url="https://your-project-demo.com",
    project_id=project1.id
)
session.add(project1_link1)
session.add(project1_link2)
```

---

### 6️⃣ **Your Social Links** (Lines 124-131)

```python
links_data = [
    {"platform": "github", "url": "https://github.com/yourusername"},
    {"platform": "linkedin", "url": "https://linkedin.com/in/yourusername"},
    {"platform": "portfolio", "url": "https://yourwebsite.com"}
]
```

---

## Step 2: Reset and Reseed the Database

After editing `seed.py`, run these commands:

### Option A: Delete and Recreate (Recommended)

```bash
# 1. Navigate to backend folder
cd backend

# 2. Activate virtual environment
venv\Scripts\activate

# 3. Delete old database
del database.db

# 4. Run seed script with your new data
python seed.py
```

### Option B: Manual Database Reset (Alternative)

If the above doesn't work, you can also:
1. Stop the backend server (Ctrl+C in the terminal)
2. Delete `backend/database.db` file manually
3. Run `python seed.py`
4. Restart the server: `uvicorn main:app --reload`

---

## Step 3: Verify Your Changes

1. **Refresh the frontend** at http://localhost:5173
2. You should see your name, bio, skills, projects, etc.
3. Test the search and filtering features

---

## 📋 Complete Example

Here's a full example with real data:

```python
def seed_database():
    """Seed the database with sample data"""
    create_db_and_tables()
    
    with Session(engine) as session:
        # Check if data already exists
        existing_profile = session.query(Profile).first()
        if existing_profile:
            print("Database already seeded. Skipping...")
            return
        
        # YOUR PROFILE
        profile = Profile(
            name="Alex Johnson",
            email="alex.johnson@email.com",
            bio="Full-stack developer with expertise in cloud architecture and DevOps",
            location="Seattle, WA"
        )
        session.add(profile)
        session.commit()
        session.refresh(profile)
        
        # YOUR SKILLS
        skills_data = ["Python", "Django", "React", "AWS", "Terraform", "Kubernetes", "PostgreSQL", "Redis"]
        for skill_name in skills_data:
            skill = Skill(name=skill_name, profile_id=profile.id)
            session.add(skill)
        
        # YOUR EDUCATION
        education = Education(
            institution="Stanford University",
            degree="Bachelor of Science",
            field_of_study="Computer Science",
            start_date="2015-09",
            end_date="2019-06",
            profile_id=profile.id
        )
        session.add(education)
        
        # YOUR WORK EXPERIENCE
        work1 = WorkExperience(
            company="Microsoft",
            position="Cloud Solutions Architect",
            description="Designed and implemented cloud infrastructure for enterprise clients",
            start_date="2021-03",
            end_date=None,
            profile_id=profile.id
        )
        session.add(work1)
        
        # YOUR PROJECTS
        project1 = Project(
            title="Cloud Migration Tool",
            description="Automated tool for migrating on-premise applications to AWS",
            technologies="Python,AWS,Terraform,Docker",
            profile_id=profile.id
        )
        session.add(project1)
        session.commit()
        session.refresh(project1)
        
        project1_link = ProjectLink(
            platform="github",
            url="https://github.com/alexj/cloud-migration-tool",
            project_id=project1.id
        )
        session.add(project1_link)
        
        # YOUR SOCIAL LINKS
        links_data = [
            {"platform": "github", "url": "https://github.com/alexjohnson"},
            {"platform": "linkedin", "url": "https://linkedin.com/in/alex-johnson"},
            {"platform": "portfolio", "url": "https://alexjohnson.dev"}
        ]
        for link_data in links_data:
            link = Link(**link_data, profile_id=profile.id)
            session.add(link)
        
        session.commit()
        print("✅ Database seeded successfully!")
```

---

## 🔧 Troubleshooting

### Issue: "Database already seeded"
**Solution:** Delete `backend/database.db` and run `python seed.py` again

### Issue: Changes not showing in UI
**Solution:** 
1. Hard refresh the browser (Ctrl+Shift+R or Cmd+Shift+R)
2. Check if backend server is running
3. Verify database was recreated

### Issue: Server errors after changing data
**Solution:** Check that:
- All strings are in quotes
- Technologies are comma-separated with no spaces: `"Python,FastAPI,React"`
- Dates are in format: `"YYYY-MM"`
- URLs are complete: `"https://..."`

---

## 💡 Pro Tips

1. **Keep it professional** - This is your portfolio API
2. **Use real project links** - GitHub repos, live demos, etc.
3. **Be specific in descriptions** - Mention technologies and impact
4. **Update regularly** - Add new projects and skills as you learn
5. **Test thoroughly** - Make sure search and filtering work with your data

---

## 🎯 Next Steps

After adding your data:
1. ✅ Test all features (search, filtering, profile display)
2. ✅ Update README.md with your resume link
3. ✅ Deploy to production (see README.md for instructions)
4. ✅ Share your API with potential employers!

---

**Need help?** Check the main README.md or the sample data in seed.py for reference.
