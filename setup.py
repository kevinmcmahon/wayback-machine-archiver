#!/usr/bin/env python

import re
from setuptools import setup, find_packages


# Get the version from the main script
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open("wayback_machine_archiver/archiver.py").read(),
    re.M,
).group(1)


# Try to import pypandoc to convert the readme, otherwise ignore it
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = ""

# Configure the package
setup(
    name="Github Pages Archiver",
    version=version,
    description="A script to backup Github Pages using the Internet Archive",
    long_description=long_description,
    author="Alexander Gude",
    author_email="alex.public.account@gmail.com",
    url="https://github.com/agude/github-pages-archiver",
    license="MIT",
    platforms=["any"],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'archiver=github_pages_archiver.archiver:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    keywords=[
        "Github Pages",
        "Internet Archive",
    ],
    install_requires=[
        'requests',
    ],
)
