# Changelog

All notable changes to HumanTyping will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-22

### Added
- 🎉 Initial release of HumanTyping
- ⌨️ Realistic typing simulation based on Markov Chains
- 🎭 Human-like typing behavior:
  - Variable typing speed (WPM configurable)
  - Natural error patterns (neighbor keys, swap errors)
  - Realistic corrections (Backspace, Arrow keys)
  - Fatigue modeling over long texts
  - Natural pauses between words
- 🚀 Playwright integration with simple API
- 🔧 Selenium integration (synchronous)
- 📚 Complete documentation:
  - README with examples
  - Quick Start guide
  - Publishing guide
  - Building guide
  - Installation guide
- 💡 4 example scripts:
  - Simple example (beginner-friendly)
  - Full Playwright example
  - Selenium example
  - Advanced features demo
- ⚙️ Configurable parameters:
  - WPM (Words Per Minute)
  - Keyboard layout (QWERTY, AZERTY)
  - Error rates
  - Speed modifiers
- 🤖 GitHub Actions CI/CD:
  - Automated testing on push
  - Automated publishing to PyPI and GitHub Releases
- 📦 Professional package structure:
  - Clean imports (`from humantyping import HumanTyper`)
  - Type hints
  - Comprehensive docstrings

### Features

#### Core Typing Simulation
- **MarkovTyper**: Semi-Markov process for realistic keystroke timing
- **Variable Speed**: Common words 40% faster, complex words 30% slower
- **Bigram Acceleration**: Frequent letter pairs typed in rapid bursts
- **Fatigue Modeling**: Gradual slowdown (0.05% per character)
- **Natural Pauses**: 250ms average between words

#### Error Patterns
- **Neighbor Errors**: Types adjacent keys based on physical keyboard layout
- **Swap Errors**: Character inversions (1.5% probability)
- **Delayed Detection**: Some errors noticed only during proofreading
- **Correction Behavior**: Immediate backspace or arrow key navigation

#### Playwright Integration
- `HumanTyper.type(element, text)` - Simple async method
- Full support for Playwright Locators and ElementHandles
- Preserves all error and correction behaviors

#### Selenium Integration
- `HumanTyper.type_sync(element, text)` - Synchronous method
- Compatible with Selenium WebElements
- Same realistic behavior as Playwright

### Installation

```bash
pip install humantyping[playwright]
```

### Quick Start

```python
from humantyping import HumanTyper
from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://google.com")
        
        typer = HumanTyper(wpm=70)
        search_box = page.locator("[name='q']")
        await search_box.click()
        await typer.type(search_box, "Hello!")
        
        await browser.close()

asyncio.run(main())
```

---

## [Unreleased]

### Planned
- [ ] Additional keyboard layouts (Dvorak, Colemak)
- [ ] Language-specific models (French, Spanish, German)
- [ ] Time-of-day fatigue patterns
- [ ] Muscle memory for repeated phrases
- [ ] Copy-paste detection avoidance
- [ ] Custom error rate profiles
- [ ] Typing style presets (beginner, average, expert)

---

## Release Notes

### How to Read Version Numbers

- **Major (X.0.0)**: Breaking changes, incompatible API changes
- **Minor (1.X.0)**: New features, backwards compatible
- **Patch (1.0.X)**: Bug fixes, backwards compatible

### Links

- [PyPI Page](https://pypi.org/project/humantyping/)
- [GitHub Repository](https://github.com/Lax3n/HumanTyping)
- [GitHub Releases](https://github.com/Lax3n/HumanTyping/releases)
- [Documentation](https://github.com/Lax3n/HumanTyping#readme)

---

**Note:** This project follows [Semantic Versioning](https://semver.org/).
