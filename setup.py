from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="data-analyst-agent",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A data analysis and visualization API using LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/data-analyst-agent",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'fastapi>=0.68.0',
        'uvicorn>=0.15.0',
        'pandas>=1.3.0',
        'numpy>=1.21.0',
        'plotly>=5.3.0',
        'python-dotenv>=0.19.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'pytest-cov>=2.0.0',
            'black>=21.0',
            'flake8>=3.9.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'data-analyst-agent=app.main:main',
        ],
    },
)
