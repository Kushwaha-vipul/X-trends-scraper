import { useState } from "react";
import { fetchTrends, runScraper } from "../services/api";
import TrendCard from "../components/TrendCard";

export default function Dashboard() {
  const [trends, setTrends] = useState([]);
  const [loading, setLoading] = useState(false);
  const [scraperLoading, setScraperLoading] = useState(false);
  const [lastRun, setLastRun] = useState(null);
  const [ip, setIp] = useState("");

  
  function toTrendArray(obj) {
    return [obj.trend1, obj.trend2, obj.trend3, obj.trend4, obj.trend5].filter(Boolean);
  }

 const handleFetch = async () => {
  setLoading(true);
  try {
    const dataArr = await fetchTrends(); 
    
    const data = Array.isArray(dataArr) && dataArr.length ? dataArr[dataArr.length - 1] : null;
    if (data) {
      setTrends([data.trend1, data.trend2, data.trend3, data.trend4, data.trend5]);
      setLastRun(data.finished_at);
      setIp(data.ip_address);
    } else {
      setTrends([]);
      setLastRun(null);
      setIp("");
    }
  } catch (err) {
    console.error(err);
  }
  setLoading(false);
};

  const handleRunScraper = async () => {
    setScraperLoading(true);
    try {
      const data = await runScraper();
      alert(data.message || "Scraper started!");
    } catch (err) {
      alert("Failed to start scraper");
      console.error(err);
    }
    setScraperLoading(false);
  };

  return (
    <div className="p-6">
      <div className="flex flex-row gap-4">
        <button
          onClick={handleFetch}
          disabled={loading}
          className="bg-blue-600 text-white px-4 py-2 rounded-lg shadow hover:bg-blue-700"
        >
          {loading ? "Fetching..." : "Fetch Latest Trends"}
        </button>
        <button
          onClick={handleRunScraper}
          disabled={scraperLoading}
          className="bg-green-600 text-white px-4 py-2 rounded-lg shadow hover:bg-green-700"
        >
          {scraperLoading ? "Running..." : "Run Selenium Script"}
        </button>
      </div>

      {lastRun && (
        <div className="mt-4 text-gray-600">
          <p><strong>Last Run:</strong> {new Date(lastRun).toLocaleString()}</p>
          <p><strong>IP Address:</strong> {ip}</p>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-6">
        {trends.map((t, i) => (
          <TrendCard key={i} trend={t} index={i} />
        ))}
      </div>
    </div>
  );
}
