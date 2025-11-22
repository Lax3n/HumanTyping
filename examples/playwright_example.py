import asyncio
from playwright.async_api import async_playwright
from humantyping.integration import HumanTyper
import os

async def main():
    print("Launching browser...")
    async with async_playwright() as p:
        # Headless=True for the agent environment
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        print("Navigating to google.com...")
        await page.goto("https://google.com")
        
        # Create a HumanTyper instance
        human = HumanTyper(wpm=70)
        
        # Locate the input field - Google uses textarea now often, but let's be robust
        # Trying a generic selector for the search bar
        search_box = page.locator("[name='q']")
        
        # Reject cookies if needed (skip for now, just typing)
        
        print("Clicking search box...")
        await search_box.click()
        
        print("Typing with realistic human behavior...")
        # Type realistically!
        await human.type(search_box, "How to type like a human?")

        
        # Verify value
        val = await search_box.input_value()
        print(f"Typed value: {val}")
        
        await browser.close()
        print("Done.")

if __name__ == "__main__":
    asyncio.run(main())
