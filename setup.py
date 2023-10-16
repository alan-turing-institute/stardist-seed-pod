#!/usr/bin/env python
from setuptools import find_packages, setup

requirements = []
with open("requirements.txt") as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup(
    name="stardist-seed-pod",
    version="0.0.1",
    description="stardist_seedpod_scivision",
    author="Evangeline Corcoran",
    author_email="ecorcoran@turing.ac.uk",
    url="https://github.com/alan-turing-institute/stardist-seed-pod",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.9",
)