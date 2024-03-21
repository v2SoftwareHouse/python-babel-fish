from setuptools import find_packages, setup

setup(
    name='BabelFish',
    packages=find_packages(include=['BabelFish']),
    version='0.0.1',
    description='A framework to drive a clean code',
    author='v2SoftwareHouse',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
