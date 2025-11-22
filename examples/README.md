# HumanTyping Examples 📚

This folder contains practical examples of using HumanTyping with different frameworks.

## 🚀 Getting Started

### 1. Install the package

```bash
# From the root directory
pip install -e .[playwright]
```

### 2. Run an example

```bash
# Simple example (recommended for beginners)
python examples/simple_example.py

# Full Playwright example
python examples/playwright_example.py

# Selenium example
python examples/selenium_example.py
```

## 📄 Available Examples

### `simple_example.py` - ⭐ Start Here!

The **simplest possible** example. Perfect for beginners.

```python
from humantyping import HumanTyper

typer = HumanTyper(wpm=70)
await typer.type(element, "Hello world!")
```

**What it does:**
- Opens Google
- Types a search query with realistic behavior
- Shows you how simple the API is

**Run it:**
```bash
python examples/simple_example.py
```

---

### `playwright_example.py` - Full Featured

A more complete example with error handling and validation.

**Features:**
- Custom WPM configuration
- Input validation
- Real-world Google search scenario

**Run it:**
```bash
python examples/playwright_example.py
```

---

### `selenium_example.py` - Selenium Support

Shows how to use HumanTyping with Selenium (synchronous).

**Features:**
- Synchronous API (`type_sync`)
- Compatible with selenium WebDriver
- Same realistic behavior

**Run it:**
```bash
python examples/selenium_example.py
```

---

## 🎯 What to Expect

When you run these examples, you'll see:

✅ **Realistic typing speed** - Not too fast, not too slow  
✅ **Natural errors** - Occasional typos on adjacent keys  
✅ **Human-like corrections** - Backspace when mistakes happen  
✅ **Variable pace** - Faster for common words, slower for complex ones  
✅ **Natural pauses** - Brief delays between words  

## 🛠️ Customization

All examples can be customized by adjusting the WPM:

```python
# Slow typer
slow_typer = HumanTyper(wpm=40)

# Average typer (default)
normal_typer = HumanTyper(wpm=60)

# Fast typer
fast_typer = HumanTyper(wpm=90)

# Pro typer
pro_typer = HumanTyper(wpm=120)
```

## 💡 Tips

1. **Start with `simple_example.py`** - It's the easiest to understand
2. **Watch the typing in action** - Run with `headless=False` to see it work
3. **Experiment with WPM** - Try different speeds to match your use case
4. **Check the console output** - Examples print helpful information

## 🐛 Troubleshooting

### "Module not found: humantyping"

**Solution:** Install the package first:
```bash
pip install -e .[playwright]
```

### "Playwright not installed"

**Solution:** Install Playwright:
```bash
pip install playwright
playwright install chromium
```

### Example runs too fast / too slow

**Solution:** Adjust the WPM in the code:
```python
typer = HumanTyper(wpm=80)  # Change this value
```

---

## 📖 More Resources

- 🚀 [Quick Start Guide](../QUICKSTART.md)
- 📚 [Full README](../README.md)
- 💬 [GitHub Issues](https://github.com/yourusername/HumanTyping/issues)

---

**Happy typing! 🎉**
