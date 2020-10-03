import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magicformulas-petrtsv",  # Replace with your own username
    version="0.0.1",
    author="Petr Tsvetkov",
    author_email="petr.tsv@gmail.com",
    description="A python package package for managing formulas and computing errors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
