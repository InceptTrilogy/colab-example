"""Setup file for the gen_fix_cycle package."""

from setuptools import setup, find_packages

setup(
    name="gen_fix_cycle",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",  # More permissive Python version
    install_requires=[
        "jupyter",
        "notebook",
        "ipykernel",
        "mypy",
        "pytest",
        "pytest-cov",
        "black",
        "isort",
        "pyright",
        "anthropic"
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "mypy",
            "pyright",
            "pytest",
            "pytest-cov"
        ]
    }
)
