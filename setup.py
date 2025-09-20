from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path)->List[str]:
    """
    Reads the requirements from a file and returns them as a list of strings.
    """
    with open(file_path) as f:
        requirements = f.readlines()
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]

    if "-e ." in requirements:
        requirements.remove("-e .")

    return requirements

setup(
    name='my_package',
    version='0.0.1',
    author='PW',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)