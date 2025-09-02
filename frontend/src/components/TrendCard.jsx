export default function TrendCard({ trend, index }) {
  return (
    <div className="bg-white shadow-md rounded-lg p-4">
      <h2 className="text-lg font-semibold">#{index + 1}</h2>
      <p className="text-gray-700">{trend || "N/A"}</p>
    </div>
  );
}
