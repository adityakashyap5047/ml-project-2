'''
The setup.py file is an essential part of packaging and distributing Python projects.
It is used by setuptools (or distutils in older Python versions) to define the 
configuration of our project, such as its metadata, dependencies, and more.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
        This function will return list of requirements
    '''

    try:
        requirement_list:List[str] = []
        with open('requirements.txt', "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

        return requirement_list
    except FileNotFoundError:
        print("requirements.txt not found")

setup(
    name='NetworkSecurity',
    version="0.0.0.1",
    author="Aditya Kumar",
    author_email="adityakumar20050510@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)