from playwright.async_api import async_playwright

async def scrape_website(url: str) -> str:
    
    async with async_playwright() as p:
        
        # Line 10: Launch an invisible browser.
        browser = await p.chromium.launch(headless=True)
        
        # Line 12: Open a new tab in that invisible browser.
        page = await browser.new_page()
        await page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            
            text_content = await page.evaluate("document.body.innerText")
            
            clean_text = " ".join(text_content.split())
            
            return clean_text
            
        except Exception as e:
            return f"Error scraping website: {str(e)}"
            
        finally:
            await browser.close()