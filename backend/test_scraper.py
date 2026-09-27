# This is a simple script to test our scraper tool.
import asyncio
from scraper import scrape_website

async def main():
    print("🚀 Starting scraper... (This might take 5 seconds)")
    
    # We are scraping a real, heavy website (Wikipedia)
    url_to_scrape = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    
    # Call our async function and wait for the result
    result = await scrape_website(url_to_scrape)
    
    # Print the first 500 characters so we can see it worked
    print("\n✅ Scraping successful! Here is a snippet of the text:")
    print("-" * 50)
    print(result[:500]) 
    print("-" * 50)

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())