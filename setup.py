from setuptools import setup, find_packages

setup(
    name='pixx_skyblock_api',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'py-cord', 'aiohttp', 'pillow', 'requests'
    ],
)
