from fastapi import APIRouter
import os
import subprocess

router = APIRouter(
    prefix="/api/scraper",
    tags=["scraper"]
)

@router.post("/")
def run_scraper():
    """
    Endpoint to trigger scraper.py script asynchronously using virtualenv python
    """
    venv_python = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")  
    subprocess.Popen([venv_python, "app/scraper.py"])
    return {"message": "Scraper started successfully"}
