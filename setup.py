from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements file and returns a list of requirements.
    It removes any line containing '-e .' which is used for editable installations.
    
    Args:
        file_path (str): The path to the requirements file.
        
    Returns:
        List[str]: A list of package requirements.
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        lines = file_obj.readlines()
        requirements = [req.strip() for req in lines]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Keshav',
    author_email='keshavjangid301@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
