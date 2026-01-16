# Me-API Playground

A personal profile API playground built with **FastAPI** (Python) backend and **React** (TypeScript) frontend. This application stores and exposes candidate profile information including skills, projects, education, and work experience through a RESTful API with a beautiful, interactive frontend.

## 🏗️ Architecture

```
project1/
├── backend/           # Python FastAPI application
│   ├── main.py       # FastAPI app with all endpoints
│   ├── models.py     # SQLModel database models
│   ├── database.py   # Database connection setup
│   ├── seed.py       # Database seeding script
│   ├── requirements.txt
│   └── database.db   # SQLite database (created after seeding)
│
└── frontend/         # React + TypeScript + Vite
    ├── src/
    │   ├── App.tsx   # Main application component
    │   ├── api.ts    # API client
    │   ├── main.tsx  # Entry point
    │   └── index.css # Global styles
    ├── index.html
    ├── package.json
    └── vite.config.ts
```

## 🚀 Tech Stack

### Backend
- **Python 3.x** - Programming language
- **FastAPI** - Modern web framework for building APIs
- **SQLModel** - SQL database ORM with Pydantic validation
- **SQLite** - Lightweight database
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool
- **Tailwind CSS** - Utility-first CSS framework

## 📋 Database Schema

### Profile
- `id`, `name`, `email`, `bio`, `location`

### Skill
- `id`, `name`, `profile_id` (FK)

### Project
- `id`, `title`, `description`, `technologies`, `profile_id` (FK)

### ProjectLink
- `id`, `platform`, `url`, `project_id` (FK)

### Education
- `id`, `institution`, `degree`, `field_of_study`, `start_date`, `end_date`, `profile_id` (FK)

### WorkExperience
- `id`, `company`, `position`, `description`, `start_date`, `end_date`, `profile_id` (FK)

### Link
- `id`, `platform`, `url`, `profile_id` (FK)

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 18+
- npm or yarn

### Local Development Setup

#### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Seed the database with sample data
python seed.py

# Run the backend server
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`

#### 2. Frontend Setup

```bash
# Navigate to frontend directory (in a new terminal)
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 🌐 API Endpoints

### Health Check
- `GET /health` - Returns API health status

### Profile
- `GET /api/profile` - Get complete profile with all related data
- `PUT /api/profile` - Update profile information

### Projects
- `GET /api/projects` - Get all projects
- `GET /api/projects?skill=python` - Filter projects by skill/technology

### Skills
- `GET /api/skills/top?limit=10` - Get top N skills

### Search
- `GET /api/search?q=python` - Search across projects, skills, and profile

## 📝 Sample API Requests

### Using cURL

```bash
# Health check
curl http://localhost:8000/health

# Get profile
curl http://localhost:8000/api/profile

# Get projects filtered by skill
curl "http://localhost:8000/api/projects?skill=Python"

# Search
curl "http://localhost:8000/api/search?q=fastapi"
```

### Using Postman

Import the following endpoints into Postman:
- Base URL: `http://localhost:8000`
- Endpoints: `/health`, `/api/profile`, `/api/projects`, `/api/search`

## 🎨 Frontend Features

- **Profile Display** - View complete profile information
- **Skill Filtering** - Click on skills to filter projects
- **Search Functionality** - Search across projects and skills
- **Responsive Design** - Works on desktop and mobile
- **Premium UI** - Modern gradient design with smooth animations

## 🚢 Production Deployment

### Backend Deployment Options

1. **Render / Railway / Fly.io**
   - Connect your GitHub repository
   - Set build command: `pip install -r backend/requirements.txt`
   - Set start command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

2. **Heroku**
   ```bash
   # Create Procfile in backend/
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

3. **AWS / GCP / Azure**
   - Deploy using Docker container or serverless functions

### Frontend Deployment Options

1. **Vercel** (Recommended)
   ```bash
   cd frontend
   npm run build
   # Deploy dist/ folder
   ```

2. **Netlify**
   - Build command: `npm run build`
   - Publish directory: `dist`

3. **GitHub Pages**
   ```bash
   npm run build
   # Deploy dist/ folder to gh-pages branch
   ```

### Environment Variables

For production, update the API base URL in `frontend/src/api.ts`:
```typescript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
```

## 🔧 Customization

### Adding Your Own Data

Edit `backend/seed.py` to replace the sample data with your real information:
- Update profile details (name, email, bio, location)
- Add your actual skills
- Add your real projects
- Update education history
- Add work experience
- Update social links

Then re-run:
```bash
# Delete existing database
rm backend/database.db

# Re-seed with your data
python backend/seed.py
```

## 📚 Known Limitations

- Single user profile (designed for personal use)
- No authentication (suitable for public portfolio)
- SQLite database (for production, consider PostgreSQL)
- Basic search (no full-text search indexing)

## 🧪 Testing

### Backend
```bash
# Test health endpoint
curl http://localhost:8000/health

# Should return: {"status": "healthy", "message": "API is running"}
```

### Frontend
- Open `http://localhost:5173` in browser
- Verify profile loads
- Test skill filtering by clicking on skills
- Test search functionality

## 📄 License

This project is open source and available for personal and educational use.

## 👤 Resume Link

**Your Resume**: [Add your resume link here]

---

**Built with ❤️ using FastAPI and React**
