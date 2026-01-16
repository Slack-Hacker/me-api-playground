# Me-API Playground

Personal profile API with FastAPI backend and React frontend.

## Quick Start

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python seed.py
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Visit http://localhost:5173

See [README.md](README.md) for full documentation.
