from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path

# Create database directory if it doesn't exist
DB_DIR = Path(__file__).parent
DB_PATH = DB_DIR / "database.db"

# Create engine
sqlite_url = f"sqlite:///{DB_PATH}"
engine = create_engine(sqlite_url, echo=False)


def create_db_and_tables():
    """Create all tables in the database"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get a database session"""
    with Session(engine) as session:
        yield session
