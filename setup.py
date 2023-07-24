
from setuptools import find_packages, setup
from typing import List
# This setup.py file will be responsible for creating this machine learning application as a package.
# And after that, I can install this package and use it in other projects.
# I can also deploy it to PYPI (the Python library for Python packages),
# and from there anybody can install and use it.
HYPHEN_E_DOT = '-e .'
# This is for reading the requirements file


def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlProject",
    version="0.0.1",
    author="Hamza",
    author_email="hamza.official010@gmail.com",
    packages=find_packages(),
    # Convert the list of requirements into a list of strings
    install_requires=get_requirements('requirements.txt')
)
# -e . will automatically trigger setup.py file
