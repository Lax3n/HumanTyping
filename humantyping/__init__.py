"""
HumanTyping - The most realistic keyboard typing simulator
==========================================================

A library for simulating realistic human typing behavior in browser automation.
Based on Markov Chains and stochastic processes.

Quick Start with Playwright
---------------------------

    import asyncio
    from playwright.async_api import async_playwright
    from humantyping import HumanTyper

    async def main():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto("https://example.com")
            
            # Create typer
            typer = HumanTyper(wpm=70)
            
            # Type like a human!
            input_field = page.locator("input[name='search']")
            await input_field.click()
            await typer.type(input_field, "Hello, realistic typing!")
            
            await browser.close()

    asyncio.run(main())

Features
--------
- Variable speed based on word complexity
- Realistic error patterns (neighbor keys, swap errors)
- Fatigue modeling over long texts
- Natural pauses and corrections
- Support for QWERTY and AZERTY layouts

For more information, see the documentation at:
https://github.com/yourusername/HumanTyping
"""

__version__ = "1.0.0"
__author__ = "HumanTyping Contributors"
__license__ = "MIT"

from .integration import HumanTyper
from .typer import MarkovTyper
from .config import (
    DEFAULT_WPM,
    PROB_ERROR,
    PROB_SWAP_ERROR,
    SPEED_BOOST_COMMON_WORD,
    SPEED_BOOST_BIGRAM,
)

__all__ = [
    "HumanTyper",
    "MarkovTyper",
    "DEFAULT_WPM",
    "PROB_ERROR",
    "PROB_SWAP_ERROR",
    "SPEED_BOOST_COMMON_WORD",
    "SPEED_BOOST_BIGRAM",
]
