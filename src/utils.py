import os
from typing import Final
from dotenv import load_dotenv

def fetch_token() -> str:
    load_dotenv()
    TOKEN: Final[str] = os.getenv("TOKEN")
    return TOKEN