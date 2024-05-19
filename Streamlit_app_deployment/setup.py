from setuptools import setup, find_packages

setup(
    name = "spacy",
    version = "1.2.0",
    description = "Simple description",
    packages = find_packages(),
    install_requires = ['spacy']  # Example of external package
)