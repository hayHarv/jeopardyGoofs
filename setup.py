from setuptools import setup, find_packages
setup(name='jeopardy',
      version='0.1',
      packages=find_packages(),
      install_requires=['numpy', 'sqlite==3.13.0']
      )
