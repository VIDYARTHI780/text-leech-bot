import os

API_ID    = os.environ.get("API_ID", "24320085")
API_HASH  = os.environ.get("API_HASH", "a9d8e5464a5ac65180bcb48fda55ec66")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
