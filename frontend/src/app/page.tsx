
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
              <div key={comp.id} className="bg-gray-800 p-4 rounded-lg flex justify-between items-center hover:bg-gray-750 transition">
                <div>
                  <h3 className="text-xl font-bold text-white">{comp.name}</h3>
                  <a href={comp.url} target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:underline">
                    {comp.url}
                  </a>
                </div>
                <span className="text-sm text-gray-500">
                  Added: {new Date(comp.created_at).toLocaleDateString()}
                </span>
              </div>
            ))
          )}
        </div>

      </div>
    </main>
  );
}