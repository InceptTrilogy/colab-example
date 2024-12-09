from setuptools import setup, find_packages

setup(
    name="colab_example",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-auth>=2.0.0",
        "google-auth-oauthlib>=0.4.0",
        "google-auth-httplib2>=0.1.0",
        "google-api-python-client>=2.0.0",
        "pydantic>=2.0.0",
    ],
    python_requires=">=3.9",
)
