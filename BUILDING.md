# HumanTyping Package Distribution  🚀

This document explains how to build and distribute the package.

## 📦 Building the Package

### Prerequisites

```bash
pip install build twine
```

### Build

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build source and wheel distributions
python -m build
```

This creates:
- `dist/humantyping-1.0.0.tar.gz` (source distribution)
- `dist/humantyping-1.0.0-py3-none-any.whl` (wheel distribution)

## 🔍 Verify the Package

```bash
# Check with twine
twine check dist/*

# Test installation locally
pip install dist/humantyping-1.0.0-py3-none-any.whl

# Verify import
python -c "from humantyping import HumanTyper; print('✓ Works!')"
```

## 📤 Upload to PyPI

### Test PyPI (Recommended First)

```bash
# Upload to Test PyPI first
twine upload --repository testpypi dist/*

# Install from Test PyPI to verify
pip install --index-url https://test.pypi.org/simple/ humantyping
```

### Production PyPI

```bash
twine upload dist/*
```

## 🤖 Automated Publishing (Preferred)

We use GitHub Actions for automated publishing. See `PUBLISHING.md` for details.

Simply create a GitHub Release with a tag (e.g., `v1.0.0`), and the package will be automatically:
1. Built
2. Tested
3. Published to PyPI
4. Attached to GitHub Release

## 📂 What Gets Included

The package includes:
- `humantyping/` - Main package code
- `examples/` - Example scripts
- `README.md` - Documentation
- `QUICKSTART.md` - Quick start guide
- `LICENSE` - MIT License
- `CONTRIBUTING.md` - Contribution guidelines

Excluded:
- `.git/`
- `.venv/`
- `__pycache__/`
- `*.pyc`
- Development files

See `MANIFEST.in` for details.

## 🐛 Troubleshooting

### "File already exists"

You uploaded this version before. Bump the version in `pyproject.toml`.

### "Invalid distribution"

Run `twine check dist/*` to see what's wrong.

### Import fails after install

Clear pip cache:
```bash
pip uninstall humantyping
pip cache purge
pip install humantyping
```

## 📊 Package Stats

After publishing, check:
- PyPI page: https://pypi.org/project/humantyping/
- Download stats: https://pypistats.org/packages/humantyping
- GitHub Releases: https://github.com/Lax3n/HumanTyping/releases

---

For automated publishing, see **PUBLISHING.md**.
