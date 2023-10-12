from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pixx_skyblock_api",
    version="0.0.2",
    author="Pixx",
    author_email="admin@pixx.pics",
    description="Shitty api wrapper for the official hypixel skyblock api",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PixxInc/skyblock"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
)
