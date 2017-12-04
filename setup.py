from setuptools import setup

setup(
    name='pydem',
    version='1.0',
    description='Generates a 3d model of a digital elevation map from coordinates',
    license="MIT",
    author='Kevin Forrest Connors',
    author_email='kevinforrestconnors.com@gmail.com',
    url="https://github.com/kevinforrestconnors/pydem",
    packages=['pydem'],
    install_requires=['numpy', 'scipy', 'utm'],
    scripts=['bin/pydem']
)