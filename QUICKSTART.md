# Quick Start Guide - HumanTyping for Playwright

This library allows you to type like a human in your Playwright automation scripts! 🤖⌨️

## Installation

### Option 1: Install from PyPI (when published)
```bash
pip install humantyping[playwright]
```

### Option 2: Install from source (current development)
```bash
# Clone the repository
git clone https://github.com/yourusername/HumanTyping.git
cd HumanTyping

# Install with uv
uv sync --extra playwright

# Or install with pip
pip install -e .[playwright]
```

## Basic Usage

```python
import asyncio
from playwright.async_api import async_playwright
from humantyping import HumanTyper

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://example.com")
        
        # Create a human typer (default: 60 WPM)
        typer = HumanTyper()
        
        # Or customize the typing speed
        fast_typer = HumanTyper(wpm=90)
        
        # Type into any input field
        search_box = page.locator("input[name='search']")
        await search_box.click()
        await typer.type(search_box, "Hello, realistic typing!")
        
        await browser.close()

asyncio.run(main())
```

## Advanced Features

### Custom Typing Speed
```python
# Slow typer (40 WPM)
slow_typer = HumanTyper(wpm=40)

# Fast typer (100 WPM)
fast_typer = HumanTyper(wpm=100)
```

### Different Keyboard Layouts
```python
# AZERTY keyboard
azerty_typer = HumanTyper(wpm=60, layout="azerty")

# QWERTY keyboard (default)
qwerty_typer = HumanTyper(wpm=60, layout="qwerty")
```

### Real-World Example: Google Search
```python
import asyncio
from playwright.async_api import async_playwright
from humantyping import HumanTyper

async def google_search():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://google.com")
        
        typer = HumanTyper(wpm=75)
        
        # Type into Google search
        search_input = page.locator("[name='q']")
        await search_input.click()
        await typer.type(search_input, "How to automate with Playwright")
        
        # Press Enter
        await search_input.press("Enter")
        await page.wait_for_load_state("networkidle")
        
        print(f"Search results loaded for: {await page.title()}")
        await browser.close()

asyncio.run(google_search())
```

## What Makes This Realistic?

HumanTyping simulates **authentic human typing behavior**:

✅ **Variable Speed**: Common words typed faster, complex words slower  
✅ **Natural Errors**: Occasional typos on adjacent keys  
✅ **Swap Errors**: Character inversions like "teh" → "the"  
✅ **Realistic Corrections**: Uses Backspace or Arrow keys to fix mistakes  
✅ **Fatigue**: Typing slows down slightly over long texts  
✅ **Natural Pauses**: Brief delays between words  

## Configuration

You can customize the behavior by editing `src/config.py`:

```python
DEFAULT_WPM = 60              # Base typing speed
PROB_ERROR = 0.04             # 4% chance of typing errors
PROB_SWAP_ERROR = 0.015       # 1.5% swap errors
SPEED_BOOST_COMMON_WORD = 0.6 # 40% faster for common words
```

## API Reference

### `HumanTyper(wpm=60, layout="qwerty")`

Main class for realistic typing in Playwright.

**Parameters:**
- `wpm` (float): Target words per minute (default: 60)
- `layout` (str): Keyboard layout - "qwerty" or "azerty" (default: "qwerty")

**Methods:**

#### `async type(page_element, text)`

Types text into a Playwright element with human-like behavior.

**Parameters:**
- `page_element`: Playwright Locator or ElementHandle
- `text` (str): Text to type

**Example:**
```python
typer = HumanTyper(wpm=70)
await typer.type(page.locator("#username"), "john_doe")
```

## Troubleshooting

### "Element is not focused"
Make sure to click the element before typing:
```python
element = page.locator("input#field")
await element.click()  # Important!
await typer.type(element, "text")
```

### "Too slow / too fast"
Adjust the WPM parameter:
```python
# Slower
typer = HumanTyper(wpm=30)

# Faster
typer = HumanTyper(wpm=120)
```

## More Examples

Check the `examples/` folder for:
- `playwright_example.py` - Basic Playwright integration
- `selenium_example.py` - Selenium integration (sync)

## Support

- 📚 [Full Documentation](https://github.com/yourusername/HumanTyping)
- 🐛 [Report Issues](https://github.com/yourusername/HumanTyping/issues)
- 💬 [Discussions](https://github.com/yourusername/HumanTyping/discussions)

---

**Built with ❤️ and probabilities by the open-source community.**
