from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req  in requirements] # /n is replaced by ""

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) 
    return requirements
setup (
    
    name = 'Mushroom_classification',
    version = '0.0.1',
    author = 'Shashank Tripathi',
    author_email = 'shashanktripathi99@outlook.com',
    install_requires = get_requirements('requirements.txt'),
    pacakages = find_packages() # the projects will have different pacakage so this will find all the pacakages
)