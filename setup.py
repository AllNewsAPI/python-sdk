from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="allnewsapi",
    version="1.0.0",
    author="AllNewsAPI",
    author_email="contact@allnewsapi.com",
    description="A Python SDK for AllNewsAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AllNewsAPI/python-sdk",
    keywords=["news data api", "news api", "news sdk", "allnewsapi"],
    license="MIT",
    project_urls={
        "Bug Tracker": "https://github.com/AllNewsAPI/python-sdk/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "certifi>=2020.12.5",
    ],
)