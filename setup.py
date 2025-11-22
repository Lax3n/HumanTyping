"""
Setup configuration for HumanTyping
====================================

This allows the package to be installed with pip:
    pip install -e .
    pip install -e .[playwright]
    pip install -e .[selenium]
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="humantyping",
    version="1.0.0",
    author="HumanTyping Contributors",
    author_email="",
    description="The most realistic keyboard typing simulator based on Markov Chains",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lax3n/HumanTyping",
    project_urls={
        "Bug Tracker": "https://github.com/Lax3n/HumanTyping/issues",
        "Documentation": "https://github.com/Lax3n/HumanTyping",
        "Source Code": "https://github.com/Lax3n/HumanTyping",
    },
    packages=["humantyping"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
    ],
    extras_require={
        "playwright": ["playwright>=1.40.0"],
        "selenium": ["selenium>=4.0.0"],
        "dev": [
            "playwright>=1.40.0",
            "selenium>=4.0.0",
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
        ],
    },
    keywords=[
        "typing",
        "simulation",
        "markov-chain",
        "automation",
        "playwright",
        "selenium",
        "human-behavior",
        "browser-automation",
        "testing",
    ],
    license="MIT",
)
