# Contributing to HumanTyping

First off, thank you for considering contributing to HumanTyping! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, uv version)

### Suggesting Enhancements

We welcome ideas! Open an issue with:
- A clear description of the enhancement
- Why it would be useful
- If possible, a rough implementation idea

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**:
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation if needed
4. **Test your changes**: `uv run main.py "Test text" --mode demo`
5. **Commit**: `git commit -m "Add amazing feature"`
6. **Push**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/HumanTyping.git
cd HumanTyping

# Install dependencies
uv sync

# Run tests
uv run main.py "Quick test" --mode demo
uv run test_integration.py  # Playwright integration test
```

## Code Style

- Follow PEP 8 for Python code
- Use descriptive variable names
- Add comments for complex logic
- Keep functions focused and small

## Ideas for Contributions

- **New keyboard layouts** (Dvorak, Colemak, international variants)
- **Language support** (French, Spanish, German word lists and bigrams)
- **Advanced features**:
  - Time-of-day fatigue patterns
  - Muscle memory for repeated phrases
  - Auto-correct simulation
  - Multi-finger typing model
- **Testing**: Unit tests, integration tests
- **Documentation**: Tutorials, use case examples

## Questions?

Feel free to open an issue with the `question` label!

---

Thank you for helping make HumanTyping better! 🚀
