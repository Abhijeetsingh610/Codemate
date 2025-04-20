from setuptools import setup, find_packages

setup(
    name="jenix",  # Unique name for your package
    version="0.1.2",  # Update version as needed
    description="An agentic coding assistant using local LLMs from Ollama",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Abhijeet Singh",
    author_email="abhis6102003@gmail.com",  # Replace with your email
    url="https://github.com/Abhijeetsingh610/Jenix.git",  # Replace with your GitHub repo
    packages=find_packages(),
    py_modules=["jenix"],  # Ensure this matches your main script/module
    install_requires=[
        "requests>=2.25.0",
        "rich",
        "anthropic",
        "google-generativeai",
    ],
    entry_points={
        "console_scripts": [
            "jenix=jenix:main",  # Expose `jenix` as a CLI command
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)