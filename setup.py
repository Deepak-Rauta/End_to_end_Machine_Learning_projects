from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements 

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # when ever i read the lines in requirements.txt a \n lines is read that creates a problem for this i will use the below list comprehension
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(

name = 'mlproject',
version= '0.0.1',
author='Deepak',
author_email='kdeepak8250@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')

)