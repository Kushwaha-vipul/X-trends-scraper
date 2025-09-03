from fastapi import APIRouter
import os
import sys
import subprocess

router = APIRouter(
    prefix="/api/scraper",
    tags=["scraper"]
)

@router.post("/")
def run_scraper():
    venv_path = os.path.join(os.getcwd(), ".venv")
    if sys.platform == "win32":
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")
    else:
        python_executable = os.path.join(venv_path, "bin", "python")

    subprocess.Popen([python_executable, "app/scraper.py"])
    return {"message": "Scraper started successfully"}
