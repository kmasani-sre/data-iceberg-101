from setuptools import setup, find_packages

setup(
    name="pyspark_iceberg_playground",
    version="0.1.0",
    author="Kiran Masani",
    author_email="kmasani81@gmail.com",
    description="A playground repository for PySpark and Apache Iceberg integration both locally and on AWS S3.",
    long_description=open("README.md").read() if open("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/kmasani-sre/data-iceberg-101.git",

    # Automatically finds the 'src' directory and treats it as a package
    packages=find_packages(where="."),

    # Specifies that the packages are located under the root or src
    package_dir={"": "."},

    # Core dependencies required to run the project
    install_requires=[
        "pyspark==3.5.0",    # Match this with your local/cluster Spark version
        "pyiceberg==0.6.0",   # Useful for lightweight Iceberg catalog metadata operations
        "boto3",              # Required for AWS S3 and Glue interactions
    ],

    # Optional dependencies for development/testing
    extras_require={
        "dev": [
            "pytest",
            "jupyter",        # For the notebooks/ directory exploration
            "black",          # Code formatting
        ]
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)