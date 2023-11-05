# setup.py

from setuptools import setup, find_packages

setup(
    name='knapsack_algorithm',
    version='1.0.0',
    author='Tamilselvan_Arjunan',
    author_email='nishantamil@gmail.com',
    description='A python implementation of the Knapsack problem using dynamic programming.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arjunlimat/knapsack_algorithm',
    packages=find_packages(),
    install_requires=[
        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)