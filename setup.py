from setuptools import setup

setup(
    name='objDEM',
    version='1.0.0',
    description='Generates an .obj file representing a digital elevation map from coordinate input',
    license="MIT",
    author='Kevin Forrest Connors',
    author_email='kevinforrestconnors.com@gmail.com',
    url="https://github.com/kevinforrestconnors/objdem",
    packages=['objDEM'],
    install_requires=['numpy', 'scipy', 'utm'],
    scripts=['objdem/objdem']
)