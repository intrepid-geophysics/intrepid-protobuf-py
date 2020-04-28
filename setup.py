from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="intrepid-protobuf",
    version="0.0.2",
    author="Difu Wang",
    author_email="difu@intrepid-geophysics.com",
    description="Protobuf bindings for Intrepid",
    url="http://git.dfalocal/playground/intbta-4085.git",
    packages=find_packages(),
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