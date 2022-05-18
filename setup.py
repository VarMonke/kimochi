from setuptools import setup

readme = open('README.rst').read()
setup(
    name='kimochi',
    version='0.0.1',
    author='VarMonke',
    license='MIT',
    requires=['aiohttp'],
    packages=['kimochi'],
    python_requires='>=3.6',
    description='Express yourself with kimochi.',
    long_description=readme,
    long_description_content_type='text/x-rst',
)
