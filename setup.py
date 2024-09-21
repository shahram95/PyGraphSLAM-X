from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='python_package',
    version='0.0.1',
    description='Python package template',
    long_description=readme,
    # keywords=[],
    license='MIT',
    author='Shahram Najam Syed',
    packages=['python_package'],
    # install_requires=[],
    # tests_require=[],
    classifiers=['License :: OSI Approved :: MIT License', 
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3'],
    test_suite='tests'
)
