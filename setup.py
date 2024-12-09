"""Setup file for the gen_fix_cycle package."""

from setuptools import setup, find_packages

setup(
    name="gen_fix_cycle",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=[
        "jupyter>=1.0.0",
        "notebook>=7.0.6",
        "ipykernel>=6.27.1",
        "mypy>=1.7.1",
        "pytest>=7.4.3",
        "pytest-cov>=4.1.0",
        "black>=23.11.0",
        "isort>=5.12.0",
        "pyright>=1.1.339"
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
