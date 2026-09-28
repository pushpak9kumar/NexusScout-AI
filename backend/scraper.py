from playwright.sync_api import sync_playwright
import asyncio

def _scrape_sync(url: str) -> str:
    # This runs the browser synchronously in a background thread.
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Spoof the User-Agent to look like a real human
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            text_content = page.evaluate("document.body.innerText")
            clean_text = " ".join(text_content.split())
            return clean_text
        except Exception as e:
            return f"Error scraping website: {str(e)}"
        finally:
            browser.close()

async def scrape_website(url: str) -> str:
    return await asyncio.to_thread(_scrape_sync, url)