import pathlib
from setuptools import setup,find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="product_similarity",
    version="1.0.0",
    description="It squares the number",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yassamine-atn/product_similarity",
    author="Atouani Yassamine",
    author_email="atouaniyasmine1@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    
    packages = find_packages(),
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        'product_similarity': ['*.pickle', '*.model'],
    },
    install_requires=["gensim","sklearn"],
    
)