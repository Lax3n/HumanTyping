# Installation rapide - HumanTyping avec Playwright

## Pour les Développeurs

```bash
# 1. Installer le package en mode développement
pip install -e .[playwright]

# 2. Installer les navigateurs Playwright
playwright install chromium

# 3. Tester
python examples/simple_example.py
```

## Pour les Utilisateurs (quand publié sur PyPI)

```bash
# 1. Installer depuis PyPI
pip install humantyping[playwright]

# 2. Installer les navigateurs
playwright install chromium

# 3. Utiliser dans votre code
```

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
        await typer.type(search_box, "Realistic typing!")
        
        await browser.close()

asyncio.run(main())
```

## Vérification

```bash
# Vérifier l'installation
python -c "from humantyping import HumanTyper; print('✓ Installé!')"
python -c "import humantyping; print(f'Version: {humantyping.__version__}')"
```

## Problèmes Courants

### "No module named 'playwright'"

**Solution:**
```bash
pip install playwright
playwright install chromium
```

### "No module named 'humantyping'"

**Solution (développement):**
```bash
cd /path/to/HumanTyping
pip install -e .[playwright]
```

**Solution (utilisateur):**
```bash
pip install humantyping[playwright]
```

### "playwright executable not found"

**Solution:**
```bash
playwright install chromium
```

## Documentation Complète

- 🚀 **Quick Start:** `QUICKSTART.md`
- 📖 **README:** `README.md`
- 📦 **Publishing:** `PUBLISHING.md`
- 🏗️ **Building:** `BUILDING.md`
- 📝 **Summary:** `SUMMARY.md`
