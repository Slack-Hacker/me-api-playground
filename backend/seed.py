from sqlmodel import Session
from database import engine, create_db_and_tables
from models import Profile, Skill, Project, Education, WorkExperience, Link, ProjectLink


def seed_database():
    """Seed the database with sample data"""
    create_db_and_tables()
    
    with Session(engine) as session:
        # Check if data already exists
        existing_profile = session.query(Profile).first()
        if existing_profile:
            print("Database already seeded. Skipping...")
            return
        
        # Create profile
        profile = Profile(
            name="Ankit Sah",
            email="an96.sah@gmail.com",
            bio="Aspiring Software Engineer Intern with a strong foundation in computer science and a passion for building innovative solutions.",
            location="New Delhi, India"
        )
        session.add(profile)
        session.commit()
        session.refresh(profile)
        
        # Add skills
        skills_data = [
            "Python", "C/C++", "Java", "MySQL", "HTML", "CSS", "JavaScript", "Solidity",
            "React", "Django", "Flask", "FastAPI", "Streamlit", "TensorFlow", "PyTorch", 
            "Scikit-learn", "OpenCV", "NLP", "Git", "Google Colab", "Jupyter Notebook"
        ]
        for skill_name in skills_data:
            skill = Skill(name=skill_name, profile_id=profile.id)
            session.add(skill)
        
        # Add education
        education1 = Education(
            institution="National Institute of Technology Delhi (NIT Delhi)",
            degree="Bachelor of Technology",
            field_of_study="Artificial Intelligence and Data Science",
            start_date="2021-08",
            end_date=None,  # Present (expected graduation)
            profile_id=profile.id
        )
        session.add(education1)
        
        education2 = Education(
            institution="Rajkiya Pratibha Vikas Vidyalaya (RPVV), Karol Bagh",
            degree="12th Standard",
            field_of_study="Science",
            start_date="2020-01",
            end_date="2022-01",
            profile_id=profile.id
        )
        session.add(education2)
        
        education3 = Education(
            institution="Rajkiya Pratibha Vikas Vidyalaya (RPVV), Karol Bagh",
            degree="10th Standard",
            field_of_study="General",
            start_date="2018-01",
            end_date="2020-01",
            profile_id=profile.id
        )
        session.add(education3)
        
        # Add work experience / achievements
        work1 = WorkExperience(
            company="LeetCode & Competitive Programming",
            position="Data Structure and Algorithm Specialist",
            description="Solved 100+ questions on LeetCode, CodeForces, and other platforms. Strong foundation in DSA using Python.",
            start_date="2023-01",
            end_date=None,
            profile_id=profile.id
        )
        work2 = WorkExperience(
            company="CISCO Networking Basics",
            position="Networking Certification",
            description="Completed comprehensive course covering Networking basics, Protocols and networking systems.",
            start_date="2025-01",
            end_date="2025-12",
            profile_id=profile.id
        )
        work3 = WorkExperience(
            company="LinkedIn Learning - AI/ML Foundations",
            position="Machine Learning Certification",
            description="Learned core concepts of Machine Learning, Deep Learning, Computer Vision, and NLP using Python libraries such as TensorFlow and Ski-learn.",
            start_date="2024-01",
            end_date="2024-12",
            profile_id=profile.id
        )
        session.add(work1)
        session.add(work2)
        session.add(work3)
        
        # Add projects
        project1 = Project(
            title="AI Chatbot",
            description="Built a chatbot using Python and NLTK to handle campus-related queries. Implemented intent recognition, keyword extraction, and rule-based responses.",
            technologies="Python,NLTK,NLP",
            profile_id=profile.id
        )
        session.add(project1)
        session.commit()
        session.refresh(project1)
        
        project2 = Project(
            title="Smart Monitoring System",
            description="Developed a CNN-based deep learning model for detecting different objects, base reference model YOLOv8. Integrated with OpenCV, Web IP Cam, Fine tuning for specific objects, Upload detect method, real-time analysis with location.",
            technologies="Python,OpenCV,YOLOv8,CNN,Deep Learning",
            profile_id=profile.id
        )
        session.add(project2)
        session.commit()
        session.refresh(project2)
        
        project3 = Project(
            title="Expense Tracker and Management System",
            description="Designed a desktop finance management app using Python, SQLite, and Tkinter. Implemented expense logging, category-wise summaries, and a basic analytics dashboard.",
            technologies="Python,SQLite,Tkinter,GUI",
            profile_id=profile.id
        )
        session.add(project3)
        session.commit()
        session.refresh(project3)
        
        project4 = Project(
            title="SMS Spam Classifier",
            description="Created a machine learning model using Scikit-learn and NLTK to classify SMS messages as spam or ham. Used process, TF-IDF vectorization, and Naive Bayes for high accuracy.",
            technologies="Python,Scikit-learn,NLTK,Machine Learning,NLP",
            profile_id=profile.id
        )
        session.add(project4)
        session.commit()
        session.refresh(project4)
        
        project5 = Project(
            title="React Native To-Do App",
            description="Built a cross-platform to-do app in React Native for task management. Implemented features like task creation, editing, deletion, and local storage with a responsive UI.",
            technologies="React Native,JavaScript,Mobile Development",
            profile_id=profile.id
        )
        session.add(project5)
        session.commit()
        session.refresh(project5)

        # --- NEW PROJECTS TO COVER ALL SKILLS ---

        project6 = Project(
            title="Decentralized Voting System",
            description="A secure voting application built on the Ethereum blockchain. Features include candidate registration, voter verification, and tamper-proof vote counting.",
            technologies="Solidity,JavaScript,React,Web3.js,Blockchain",
            profile_id=profile.id
        )
        session.add(project6)
        session.commit()
        session.refresh(project6)

        project7 = Project(
            title="Library Management System",
            description="Robust desktop application for managing library books and members. Handles issue/return cycles, fine calculation, and generates reports using a relational database.",
            technologies="Java,MySQL,JDBC,Swing",
            profile_id=profile.id
        )
        session.add(project7)
        session.commit()
        session.refresh(project7)

        project8 = Project(
            title="High-Performance Matrix Multiplier",
            description="Optimized matrix multiplication algorithms implemented to demonstrate memory management and pointer arithmetic. Benchmarked against standard libraries.",
            technologies="C/C++,Make,System Programming",
            profile_id=profile.id
        )
        session.add(project8)
        session.commit()
        session.refresh(project8)

        project9 = Project(
            title="E-Commerce API Service",
            description="Scalable backend service for an online store. Features JWT authentication, product catalog management, and order processing.",
            technologies="Django,Python,SQL,Rest API",
            profile_id=profile.id
        )
        session.add(project9)
        session.commit()
        session.refresh(project9)

        project10 = Project(
            title="Weather Forecasting Microservice",
            description="Lightweight API that fetches real-time weather data and provides forecasted trends. Deployed using Docker containers for portability.",
            technologies="Flask,Python,Docker,API,Git",
            profile_id=profile.id
        )
        session.add(project10)
        session.commit()
        session.refresh(project10)

        project11 = Project(
            title="Stock Price Predictor Dashboard",
            description="Interactive web dashboard for visualizing stock trends and predicting future prices using deep learning models.",
            technologies="Streamlit,TensorFlow,Python,Pandas",
            profile_id=profile.id
        )
        session.add(project11)
        session.commit()
        session.refresh(project11)

        project12 = Project(
            title="Image Classification Research",
            description="Research notebook demonstrating state-of-the-art image classification techniques. documented experiments with different hyperparameters.",
            technologies="PyTorch,Jupyter Notebook,Google Colab,Computer Vision",
            profile_id=profile.id
        )
        session.add(project12)
        session.commit()
        session.refresh(project12)

        project13 = Project(
            title="Personal Portfolio Website",
            description="Responsive personal portfolio website to showcase projects and skills. Implemented modern design principles and semantic markup.",
            technologies="HTML,CSS,JavaScript,Git,Responsive Design",
            profile_id=profile.id
        )
        session.add(project13)
        session.commit()
        session.refresh(project13)
        
        project14 = Project(
            title="FastAPI User Authentication System",
            description="High-performance authentication microservice. Implements OAuth2 with JWT tokens, password hashing, and role-based access control.",
            technologies="FastAPI,Python,SQLAlchemy,AsyncIO",
            profile_id=profile.id
        )
        session.add(project14)
        session.commit()
        session.refresh(project14)

        # --- CLONE PROJECTS ---

        project15 = Project(
            title="Netflix Clone",
            description="A pixel-perfect clone of Netflix with movie trailers (TMDB API), user authentication, and 'My List' feature. Optimized for performance and responsiveness.",
            technologies="React,Redux,Firebase,TMDB API,Tailwind CSS",
            profile_id=profile.id
        )
        session.add(project15)
        session.commit()
        session.refresh(project15)

        project16 = Project(
            title="Amazon Clone",
            description="Full-stack e-commerce replica with user authentication, product basket, and Stripe payment processing. key functionality including checkout pipeline.",
            technologies="React,Node.js,Express,Stripe API,Firebase Auth",
            profile_id=profile.id
        )
        session.add(project16)
        session.commit()
        session.refresh(project16)
        
        session.refresh(project16)
        
        # --- HTML/CSS PROJECTS ---

        project17 = Project(
            title="Modern Lo-Fi Landing Page",
            description="A high-conversion landing page featuring a modern lo-fi aesthetic. Built with semantic HTML5 and advanced CSS3 animations (keyframes, transitions).",
            technologies="HTML,CSS,Flexbox,Responsive Design",
            profile_id=profile.id
        )
        session.add(project17)
        session.commit()
        session.refresh(project17)

        project18 = Project(
            title="CSS Art Gallery",
            description="A collection of artistic shapes and illustrations created entirely with Code. Demonstrates mastery of CSS pseudo-elements, gradients, and box-shadows without any images.",
            technologies="HTML,CSS,Pure CSS,Art",
            profile_id=profile.id
        )
        session.add(project18)
        session.commit()
        session.refresh(project18)

        project19 = Project(
            title="Grid Dashboard UI",
            description="A complex admin dashboard layout built exclusively with CSS Grid. Features a responsive sidebar, data widgets, and a layout that adapts seamlessly to mobile screens.",
            technologies="HTML,CSS,CSS Grid,UI Design",
            profile_id=profile.id
        )
        session.add(project19)
        session.commit()
        session.refresh(project19)

        project20 = Project(
            title="Parallax Scrolling Website",
            description="An immersive storytelling website utilizing CSS parallax effects and Scroll Snap API. Creates a depth-filled user experience without heavy JavaScript libraries.",
            technologies="HTML,CSS,Parallax,Web Design",
            profile_id=profile.id
        )
        session.add(project20)
        session.commit()
        session.refresh(project20)

        project21 = Project(
            title="Responsive Email Templates",
            description="A suite of cross-client compatible HTML email templates. Rigorously tested for rendering consistency across Outlook, Gmail, and Apple Mail.",
            technologies="HTML,CSS,Email Design,Table Layouts",
            profile_id=profile.id
        )
        session.add(project21)
        session.commit()
        session.refresh(project21)

        # Add social links
        links_data = [
            {"platform": "github", "url": "https://github.com/Slack-Hacker"},
            {"platform": "linkedin", "url": "https://www.linkedin.com/in/slack-hacker"},
            {"platform": "resume", "url": "https://drive.google.com/file/d/1DGYEl4zCxXKwzK-0sJ9XAcHSqe0zmTCy/view"}
        ]
        for link_data in links_data:
            link = Link(**link_data, profile_id=profile.id)
            session.add(link)
        
        session.commit()
        print("✅ Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
