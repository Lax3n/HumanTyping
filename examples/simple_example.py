"""
Simple HumanTyping example with Playwright
==========================================

This is the SIMPLEST way to use HumanTyping with Playwright.
Perfect for beginners!
"""

import asyncio
from playwright.async_api import async_playwright
from humantyping import HumanTyper

async def main():
    # Launch browser
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Navigate to any website
        await page.goto("https://google.com")
        
        # Create a human typer (it's that simple!)
        typer = HumanTyper(wpm=70)
        
        # Find the input field and type like a human
        search_box = page.locator("[name='q']")
        await search_box.click()
        
        # The magic happens here! 🎩✨
        await typer.type(search_box, "Playwright automation tutorial")
        
        # Wait to see the result
        await asyncio.sleep(2)
        
        await browser.close()
        print("✅ Done! Check how realistic that was!")

if __name__ == "__main__":
    asyncio.run(main())
