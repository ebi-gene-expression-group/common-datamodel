import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="common-datamodel",
    version="0.0.1",
    author="Anja Füllgrabe",
    author_email="anjaf@ebi.ac.uk",
    description="Data model to describe functional genomics experimental metadata",
    license="Apache Software License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebi-gene-expression-group/common_datamodel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    include_package_data=True,
    python_requires=">=3.6",
)
