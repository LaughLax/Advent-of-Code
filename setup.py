from setuptools import find_packages, setup

setup(
    name='Advent-of-Code',
    version='1.0.0',
    description='Advent of Code Solutions',
    author='David Haralson',
    author_email='LaughLax@gmail.com',
    url='https://github.com/LaughLax/Advent-of-Code',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'networkx',
        'tqdm',
        'regex',
    ]
)
