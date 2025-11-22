"""
Advanced HumanTyping Example
=============================

This example demonstrates advanced features and customization options.
"""

import asyncio
from playwright.async_api import async_playwright
from humantyping import HumanTyper

async def main():
    print("🚀 Advanced HumanTyping Demo\n")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Navigate to a form page
        await page.goto("https://www.google.com/forms/about/")
        print("✓ Navigated to Google Forms\n")
        
        # Example 1: Different typing speeds
        print("Example 1: Different Typing Speeds")
        print("-" * 40)
        
        slow_typer = HumanTyper(wpm=40)
        normal_typer = HumanTyper(wpm=70)
        fast_typer = HumanTyper(wpm=100)
        
        print(f"Slow typer:   {slow_typer.wpm} WPM")
        print(f"Normal typer: {normal_typer.wpm} WPM")
        print(f"Fast typer:   {fast_typer.wpm} WPM\n")
        
        # Example 2: Multiple input fields
        print("Example 2: Filling Multiple Fields")
        print("-" * 40)
        
        await page.goto("https://www.google.com")
        
        # Create a typer for this session
        typer = HumanTyper(wpm=75)
        
        # Type into search box
        search_box = page.locator("[name='q']")
        await search_box.click()
        
        print("Typing search query...")
        await typer.type(search_box, "realistic typing simulation")
        print("✓ Typed search query\n")
        
        await asyncio.sleep(2)
        
        # Clear and type again
        await search_box.press("Control+A")
        await asyncio.sleep(0.2)
        
        print("Typing new query with different speed...")
        fast_typer = HumanTyper(wpm=95)
        await fast_typer.type(search_box, "playwright automation")
        print("✓ Typed with faster speed\n")
        
        await asyncio.sleep(2)
        
        # Example 3: Different keyboard layout
        print("Example 3: AZERTY Keyboard Layout")
        print("-" * 40)
        
        azerty_typer = HumanTyper(wpm=60, layout="azerty")
        print(f"Using layout: {azerty_typer.layout}")
        
        await search_box.press("Control+A")
        await asyncio.sleep(0.2)
        await azerty_typer.type(search_box, "AZERTY keyboard test")
        print("✓ Typed with AZERTY layout\n")
        
        await asyncio.sleep(2)
        
        # Example 4: Simulating different user personas
        print("Example 4: User Personas")
        print("-" * 40)
        
        personas = {
            "Beginner": HumanTyper(wpm=35),
            "Average User": HumanTyper(wpm=60),
            "Professional": HumanTyper(wpm=85),
            "Expert Typist": HumanTyper(wpm=110),
        }
        
        for persona_name, persona_typer in personas.items():
            print(f"{persona_name:20} - {persona_typer.wpm} WPM")
        print()
        
        # Example 5: Long text simulation
        print("Example 5: Long Text (with Fatigue)")
        print("-" * 40)
        
        long_text = (
            "This is a longer piece of text that will demonstrate "
            "the fatigue modeling feature. As the typing continues, "
            "the speed will gradually decrease, simulating real human behavior. "
            "This makes the automation much more realistic and harder to detect."
        )
        
        await search_box.press("Control+A")
        await asyncio.sleep(0.2)
        
        print("Typing long text (watch the gradual slowdown)...")
        await normal_typer.type(search_box, long_text)
        print("✓ Completed long text typing\n")
        
        await asyncio.sleep(3)
        
        # Summary
        print("\n" + "=" * 50)
        print("✨ Demo Complete!")
        print("=" * 50)
        print("\nKey Features Demonstrated:")
        print("  ✓ Variable typing speeds (WPM)")
        print("  ✓ Multiple keyboard layouts")
        print("  ✓ User personas")
        print("  ✓ Fatigue modeling over long texts")
        print("  ✓ Natural errors and corrections")
        print("\nTry adjusting the WPM values to see the difference!")
        print()
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
