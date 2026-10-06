import os
from pathlib import Path
from dotenv import load_dotenv

# Base filesystem directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FRONTEND_DIR = BASE_DIR / "frontend"

# Ensure data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Load environment variables
load_dotenv(BASE_DIR / ".env")

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Competitive Intelligence Agent")
    APP_SUBTITLE: str = os.getenv(
        "APP_SUBTITLE", 
        "An AI agent that remembers competitor moves and uncovers strategic patterns."
    )
    
    # Hindsight by Vectorize Configuration
    HINDSIGHT_BASE_URL: str = os.getenv("HINDSIGHT_BASE_URL", "http://localhost:8888")
    HINDSIGHT_API_KEY: str | None = os.getenv("HINDSIGHT_API_KEY", None) or None
    HINDSIGHT_BANK_ID: str = os.getenv("HINDSIGHT_BANK_ID", "competitive-intelligence-bank")
    FORCE_LOCAL_MEMORY: bool = os.getenv("FORCE_LOCAL_MEMORY", "false").lower() in ("true", "1", "yes")

    # LLM / AI Configuration
    GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY", None) or None
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY", None) or None
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "auto")

    # Local Persistence
    DATA_PATH: Path = DATA_DIR
    LOCAL_STORAGE_FILE: Path = DATA_DIR / "memory_store.json"
    
    # Server Host & Port
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

settings = Settings()
