from setuptools import setup, find_packages
from HTMLEntity import __version__

README = open('README.md').read()

setup(name='HTMLEntity',
      version=__version__,
      description='HTML Entities for Python',
      long_description=README,
      author='Erik Wang',
      author_email='wangjingbupt@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      )
