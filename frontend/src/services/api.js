const API_BASE = "http://127.0.0.1:8000/api";  

export async function fetchTrends() {
  const response = await fetch(`${API_BASE}/trends/`);
  if (!response.ok) throw new Error("Failed to fetch trends");
  return response.json();
}

export async function runScraper() {
  const response = await fetch(`${API_BASE}/trends/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({}) 
  });
  if (!response.ok) throw new Error("Failed to run scraper");
  return response.json();
}
