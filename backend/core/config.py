import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    AGENTCASH_API_KEY = os.getenv("AGENTCASH_API_KEY")
    AGENTCASH_SECRET = os.getenv("AGENTCASH_SECRET")

    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
    REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()