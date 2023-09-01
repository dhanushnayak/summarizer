from setuptools import setup, find_packages

with open("requirements.txt",'r') as _f:
    requirements = [line for line in _f.read().split('\n')]
    print(requirements)

with open("README.md",'r') as _f: description = _f.read()
__version__ =  0.1

name  = "Summarizer"
author = "Dhanush"
author_url =  "dhanushnayak.ram@gmail.com"
url = "https://github.com/dhanushnayak/summarizer"

setup(
    name=name,
    description=description,
    version=__version__,
    author=author,
    author_email=author_url,
    url=url,
    requires=requirements,
    entry_points="""
    [console_scripts]
    summarize=summarize.main:main
    """,
    packages=find_packages()
)
