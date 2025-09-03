from fastapi import APIRouter, Response
import os
import subprocess

router = APIRouter(
    prefix="/api/scraper",
    tags=["scraper"]
)

@router.post("/")
def run_scraper(response: Response):
    venv_python = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")  # Windows ke liye
    subprocess.Popen([venv_python, "app/scraper.py"])

    # Explicit CORS header add karo
    response.headers["Access-Control-Allow-Origin"] = "*"

    return {"message": "Scraper started successfully"}

