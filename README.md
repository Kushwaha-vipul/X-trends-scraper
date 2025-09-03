# X Trending Topics Scraper

A full-stack application that automatically scrapes the top 5 trending topics from X (formerly Twitter) and displays them on a web dashboard. This project includes:

- A Selenium-based scraper with proxy IP rotation to fetch trends.
- A Python backend service (FastAPI/Django) with PostgreSQL database storage.
- A React/Next.js frontend dashboard to view the latest scraped trends.

---

## Features

- **Automated scraping:** Logs in to X with multi-step authentication handling (username, email challenge, password, verify email) using Selenium.
- **Proxy IP rotation:** Uses ProxyMesh to route requests via different IPs for each scrape.
- **Database persistence:** Stores each scrape’s unique ID, top 5 trends, timestamp, and IP address in PostgreSQL.
- **User-friendly frontend:** Fetch trends with one click and view recent scrape data (trends, date/time, IP).
- **Public deployment:** Backend API and frontend are deployed publicly for testing and demo.

---

## Repository Structure

X-TRENDS-SCRAPER/
├── backend/ # Python backend service + scraper
│ ├── app/ # Backend app modules (routers, models, scraper.py etc)
│ ├── .venv/ # Python virtual environment (ignored in git)
│ └── .env # Environment variables (ignored in git)
├── frontend/ # React/Next.js frontend app
│ ├── node_modules/ # Node.js dependencies (ignored in git)
│ ├── public/ # Static assets
│ ├── src/ # Source code files
│ └── .gitignore
├── outputScreenshot/ # Images/screenshots (if any)
├── .gitignore # Global ignore rules
└── README.md # Project documentation (this file)


---

## Setup & Local Development

### Backend

1. **Create Python virtual environment** and activate:
cd backend
python -m venv .venv
.venv\Scripts\activate


 **Install dependencies:**

pip install -r requirements.txt
**Configure environment variables:**

- Create `.env` file
- Set database URL (`DATABASE_URL=postgresql://user:password@host:port/dbname`)--------> By the way i already give .env file so no need to do it .
- Set ProxyMesh credentials or other secrets.

 **Run backend server:**

Scraper will login, fetch trends, and store them in DB.

---

### Frontend

1. **Install npm packages:**

cd frontend
npm install


**Setup environment variables:**

 **Run frontend dev server:**



## Notes & Special Instructions

- ProxyMesh integration ensures different IPs are used to avoid scraper blocks.
- Twitter login includes multi-step challenge handling (email, password, verify email).
- OTP and captcha challenges require manual intervention (currently not automated).
- Scraper results are automatically saved to Postgres and reflected on frontend.
- Use provided scripts and environment variables carefully; do not expose credentials publicly.




Thank you for reviewing my project!


#output ScreenShot

<img width="1902" height="929" alt="Screenshot 2025-09-03 000928" src="https://github.com/user-attachments/assets/92397bdb-447f-476c-b760-cfef4bd00b62" />

<img width="1891" height="909" alt="Screenshot 2025-09-03 014049" src="https://github.com/user-attachments/assets/540e7603-9dd7-4c3b-81ff-df175a39da9c" />

<img width="1058" height="929" alt="Screenshot 2025-09-03 014424" src="https://github.com/user-attachments/assets/4fdbb74f-3ad3-48f2-816f-891fec89c024" />

<img width="1001" height="905" alt="Screenshot 2025-09-03 014452" src="https://github.com/user-attachments/assets/1981f9a2-4d8f-4910-8ce9-ee106c98e49c" />

<img width="1879" height="950" alt="Screenshot 2025-09-03 003014" src="https://github.com/user-attachments/assets/cc6f5578-2a3c-4875-80ad-d63ece62a5a2" />
