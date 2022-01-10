from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="intrepid-protobuf",
    version="6.2.0",
    author="Intrepid Geophysics",
    author_email="developers@intrepid-geophysics.com",
    description="Protobuf bindings for Intrepid products",
    url="https://github.com/intrepid-geophysics/intrepid-protobuf-py.git",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'protobuf',
    ],
    python_requires='>=3.6',
)