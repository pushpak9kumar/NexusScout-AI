import asyncio
from scraper import scrape_website
from agent import analyze_competitor

async def main():
    print("🕷️ Step 1: Scraping the website...")
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence" # MUST be Wikipedia for the test 
    
    raw_text = await scrape_website(url)
    
    if "Error" in raw_text:
        print(f"❌ Scraping failed: {raw_text}")
        return
        
    print(f"✅ Scraped {len(raw_text)} characters. Sending to AI Brain...")
    
    print("🧠 Step 2: AI is thinking... (This takes about 5 seconds)")
    analysis = await analyze_competitor(raw_text)
    
    print("\n" + "="*50)
    print("🤖 AI AGENT ANALYSIS REPORT:")
    print("="*50)
    print(analysis)
    print("="*50)

if __name__ == "__main__":
    asyncio.run(main())