# Publishing HumanTyping Package 📦

This guide explains how to publish new versions of HumanTyping.

## 🎯 Publication Options

HumanTyping is published to **two locations**:

1. **PyPI** (Python Package Index) - `pip install humantyping`
2. **GitHub Releases** - Download from GitHub

Both are updated automatically via GitHub Actions when you create a release.

---

## 📋 Prerequisites

### For PyPI (First Time Only)

1. Create an account on [PyPI](https://pypi.org)
2. Set up [Trusted Publishers](https://docs.pypi.org/trusted-publishers/) on PyPI:
   - Go to your PyPI account settings
   - Add a new "pending publisher"
   - Owner: `yourusername`
   - Repository: `HumanTyping`
   - Workflow: `publish.yml`
   - Environment: `pypi`

No API tokens needed with trusted publishing! ✅

---

## 🚀 How to Publish a New Version

### 1. Update Version Number

Edit `pyproject.toml`:

```toml
[project]
name = "humantyping"
version = "1.1.0"  # <-- Update this
```

### 2. Update CHANGELOG (Optional but Recommended)

Create a `CHANGELOG.md` if you haven't already, documenting what changed.

### 3. Commit Changes

```bash
git add .
git commit -m "Release v1.1.0"
git push origin main
```

### 4. Create a Git Tag

```bash
# Create and push tag
git tag v1.1.0
git push origin v1.1.0
```

### 5. Create GitHub Release

**Option A: Via GitHub Web Interface (Recommended)**

1. Go to your repository on GitHub
2. Click **"Releases"** → **"Create a new release"**
3. Choose the tag you just created (`v1.1.0`)
4. Fill in release notes (what's new, bug fixes, etc.)
5. Click **"Publish release"**

**Option B: Via GitHub CLI**

```bash
gh release create v1.1.0 \
  --title "v1.1.0 - Feature Name" \
  --notes "- Added feature X
- Fixed bug Y
- Improved performance"
```

### 6. Automatic Publication

Once you create the release, GitHub Actions will automatically:

✅ Build the package  
✅ Publish to PyPI  
✅ Upload wheel files to GitHub Release  

Check progress at: **Actions** tab on GitHub

---

## 🔍 Verify Publication

### Check PyPI

```bash
pip install --upgrade humantyping
python -c "import humantyping; print(humantyping.__version__)"
```

Or visit: https://pypi.org/project/humantyping/

### Check GitHub Releases

Visit: `https://github.com/yourusername/HumanTyping/releases`

---

## 🛠️ Manual Publication (Fallback)

If GitHub Actions fails, you can publish manually:

### Build the package

```bash
pip install build twine
python -m build
```

### Publish to PyPI

```bash
twine upload dist/*
```

You'll need a PyPI API token for manual uploads.

---

## 📝 Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **Major** (1.0.0): Breaking changes
- **Minor** (1.1.0): New features, backwards compatible
- **Patch** (1.0.1): Bug fixes

Examples:
- `1.0.0` → `1.0.1`: Bug fix
- `1.0.1` → `1.1.0`: New feature
- `1.1.0` → `2.0.0`: Breaking change

---

## 🐛 Troubleshooting

### "Package already exists" on PyPI

You can't override an existing version. Bump the version number.

### GitHub Actions fails

1. Check the **Actions** tab for error logs
2. Ensure PyPI trusted publisher is configured correctly
3. Verify the workflow has proper permissions

### Import fails after installation

```bash
pip uninstall humantyping
pip install --no-cache-dir humantyping
```

---

## 📦 What Users Will Install

### From PyPI (Most Common)

```bash
pip install humantyping[playwright]
```

### From GitHub Releases

```bash
pip install https://github.com/yourusername/HumanTyping/releases/download/v1.0.0/humantyping-1.0.0-py3-none-any.whl
```

---

## ✅ Checklist Before Release

- [ ] Version number updated in `pyproject.toml`
- [ ] CHANGELOG.md updated
- [ ] Tests passing
- [ ] Examples work correctly
- [ ] README.md is up to date
- [ ] All changes committed
- [ ] Tag created and pushed
- [ ] Release notes prepared

---

**That's it!** 🎉 Your package will be available on PyPI and GitHub Releases.
