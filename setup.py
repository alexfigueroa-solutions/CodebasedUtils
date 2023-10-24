from setuptools import setup, find_packages

# Read the README content for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codebasedutils",
    version="0.1.0",
    packages=find_packages(),
    author="Alex Figueroa",
    author_email="cybrvybe@gmail.com",
    description="CodebasedUtils is a versatile CLI tool designed to supercharge your developer workflow.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cybrvybe/CodebasedUtils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'click',
        'colorama'
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'util=core.print_dir:util',
        ],
    }
)
