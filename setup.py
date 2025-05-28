from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of the requirements
    '''
    Hypen_e_dot='-e .'   
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements

setup(
name='Mlproject',
version='0.0.1',
author='Anurag',
author_email='anuragchowdhury0504@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
    
)