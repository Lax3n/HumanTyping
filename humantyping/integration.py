import time
import asyncio
from .typer import MarkovTyper

class HumanTyper:
    """
    A helper class to integrate realistic typing into automation frameworks like Playwright or Selenium.
    """
    def __init__(self, wpm=60.0, layout="qwerty"):
        self.wpm = wpm
        self.layout = layout

    async def type(self, page_element, text):
        """
        Types text into a Playwright element with realistic human behavior.
        
        This is the main method for Playwright integration. It simulates:
        - Variable typing speed based on word complexity
        - Realistic errors (neighbor keys, swaps)
        - Natural corrections with backspace or arrow keys
        - Fatigue over longer texts
        
        Args:
            page_element: The Playwright Locator or ElementHandle to type into.
            text: The text to type with human-like behavior.
            
        Example:
            typer = HumanTyper(wpm=70)
            input_box = page.locator("input[name='search']")
            await input_box.click()
            await typer.type(input_box, "Hello world!")
        """
        # 1. Generate the realistic keystroke sequence
        typer = MarkovTyper(text, target_wpm=self.wpm, layout=self.layout)
        _, history = typer.run()
        
        last_time = 0.0
        current_text_on_screen = ""

        for t, action, content_snapshot in history:
            # Calculate delay since last action
            delay = t - last_time
            if delay > 0:
                await asyncio.sleep(delay)
            last_time = t

            # Execute action
            if "BACKSPACE" in action:
                await page_element.press("Backspace")
                current_text_on_screen = current_text_on_screen[:-1]
            elif "TYPED_ERROR" in action:
                # Extract the wrong char typed
                char = action.split("'")[1]
                await page_element.type(char)
                current_text_on_screen += char
            elif "TYPED_SWAP" in action:
                char = action.split("'")[1]
                await page_element.type(char)
                current_text_on_screen += char
            elif "TYPED" in action:
                char = action.split("'")[1]
                await page_element.type(char)
                current_text_on_screen += char
            elif "ARROW_LEFT" in action:
                await page_element.press("ArrowLeft")
            elif "ARROW_RIGHT" in action:
                await page_element.press("ArrowRight")

    def type_sync(self, selenium_element, text):
        """
        Types text into a Selenium WebElement (or any sync object with send_keys).
        Note: Selenium send_keys usually appends, so handling backspace might need specific keys.
        """
        from selenium.webdriver.common.keys import Keys
        
        typer = MarkovTyper(text, target_wpm=self.wpm, layout=self.layout)
        _, history = typer.run()
        
        last_time = 0.0
        
        for t, action, _ in history:
            delay = t - last_time
            if delay > 0:
                time.sleep(delay)
            last_time = t

            if "BACKSPACE" in action:
                selenium_element.send_keys(Keys.BACK_SPACE)
            elif "ARROW_LEFT" in action:
                selenium_element.send_keys(Keys.ARROW_LEFT)
            elif "ARROW_RIGHT" in action:
                selenium_element.send_keys(Keys.ARROW_RIGHT)
            elif "TYPED" in action: # Handles TYPED, TYPED_ERROR, TYPED_SWAP
                char = action.split("'")[1]
                selenium_element.send_keys(char)
