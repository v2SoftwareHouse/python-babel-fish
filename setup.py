from setuptools import find_packages, setup

import package_obfuscator
package_obfuscator.obfuscate('src', output='BabelFish')

setup(
    name='BabelFish',
    packages=find_packages(include=['BabelFish', 'BabelFish.*']),
    version='0.0.1',
    description='My first Python library',
    author='Me',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)