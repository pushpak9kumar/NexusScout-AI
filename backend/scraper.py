from playwright.async_api import async_playwright

async def scrape_website(url: str) -> str:
    
    async with async_playwright() as p:
        
        # Line 10: Launch an invisible browser.
        browser = await p.chromium.launch(headless=True)
        
        # Line 12: Open a new tab in that invisible browser.
        page = await browser.new_page()
        
        try:
            await page.goto(url, wait_until="networkidle", timeout=30000)
            
            text_content = await page.evaluate("document.body.innerText")
            
            clean_text = " ".join(text_content.split())
            
            return clean_text
            
        except Exception as e:
            return f"Error scraping website: {str(e)}"
            
        finally:
            await browser.close()