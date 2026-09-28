"use client";

import { useState, useEffect } from "react";

interface Competitor {
  id: number;
  name: string;
  url: string;
  created_at: string;
}

export default function Home() {
  const [competitors, setCompetitors] = useState<Competitor[]>([]);
  const [name, setName] = useState("");
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  
  // New states for the AI Scanner
  const [scanningId, setScanningId] = useState<number | null>(null);
  const [analysis, setAnalysis] = useState<string>("");

  useEffect(() => {
    fetchCompetitors();
  }, []);

  const fetchCompetitors = async () => {
    const res = await fetch("http://127.0.0.1:8000/competitors");
    const data = await res.json();
    setCompetitors(data);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    await fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, url }),
    });

    setName("");
    setUrl("");
    fetchCompetitors();
    setLoading(false);
  };

  // NEW: The function to trigger the AI Agent
  const handleScan = async (competitor: Competitor) => {
    setScanningId(competitor.id);
    setAnalysis(""); // Clear previous analysis
    
    try {
      // Call our new /scan endpoint
      const res = await fetch("http://127.0.0.1:8000/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: competitor.url }), 
      });

      if (!res.ok) throw new Error("Scan failed");
      
      const data = await res.json();
      setAnalysis(data.analysis); // Save the AI's Markdown report
    } catch (error) {
      setAnalysis("❌ Failed to scan. The website might be blocking bots.");
    } finally {
      setScanningId(null);
    }
  };

  return (
    <main className="min-h-screen bg-gray-900 text-white p-8">
      <div className="max-w-4xl mx-auto">
        
        {/* Header */}
        <h1 className="text-4xl font-bold mb-2 text-blue-400">NexusScout AI</h1>
        <p className="text-gray-400 mb-8">Autonomous Competitor Intelligence Dashboard</p>

        {/* Add Competitor Form */}
        <form onSubmit={handleSubmit} className="bg-gray-800 p-6 rounded-lg shadow-lg mb-8 flex gap-4">
          <input
            type="text"
            placeholder="Company Name (e.g., Zomato)"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="flex-1 p-3 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
          <input
            type="url"
            placeholder="Website URL (e.g., https://zomato.com)"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="flex-1 p-3 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
          <button 
            type="submit" 
            disabled={loading}
            className="px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded font-semibold transition disabled:opacity-50"
          >
            {loading ? "Adding..." : "Add Competitor"}
          </button>
        </form>

        {/* Competitors List */}
        <h2 className="text-2xl font-semibold mb-4">Tracked Competitors ({competitors.length})</h2>
        <div className="space-y-4">
          {competitors.length === 0 ? (
            <p className="text-gray-500 text-center py-8">No competitors added yet. Add one above!</p>
          ) : (
            competitors.map((comp) => (
              <div key={comp.id} className="bg-gray-800 p-6 rounded-lg shadow-md border border-gray-700">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="text-xl font-bold text-white">{comp.name}</h3>
                    <a href={comp.url} target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:underline text-sm">
                      {comp.url}
                    </a>
                  </div>
                  
                  {/* Run AI Scan Button */}
                  <button
                    onClick={() => handleScan(comp)}
                    disabled={scanningId === comp.id}
                    className="px-4 py-2 bg-purple-600 hover:bg-purple-700 rounded font-semibold text-sm transition flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {scanningId === comp.id ? (
                      <span>🤖 Scanning...</span>
                    ) : (
                      <span>🤖 Run AI Scan</span>
                    )}
                  </button>
                </div>

                {/* Display the AI Analysis */}
                {analysis && scanningId !== comp.id && (
                  <div className="mt-4 p-4 bg-gray-900 rounded border border-purple-500/30">
                    <h4 className="text-purple-400 font-semibold mb-2 flex items-center gap-2">
                      📊 AI Intelligence Report:
                    </h4>
                    {/* whitespace-pre-wrap preserves the Markdown line breaks perfectly */}
                    <pre className="text-gray-300 text-sm whitespace-pre-wrap font-sans leading-relaxed">
                      {analysis}
                    </pre>
                  </div>
                )}
              </div>
            ))
          )}
        </div>

      </div>
    </main>
  );
}