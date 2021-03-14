import os
import sys
from setuptools import setup, find_packages


__author__ = 'Itay Aveksis'
__email__ = 'itayav@nvidia.com'
__package_name__ = 'pynetest'

if sys.version_info < (3, 6):
    sys.exit(f'{__package_name__} requires Python 3.6 or higher')

path = os.path.dirname(__file__)
exec(open(os.path.join(path, __package_name__, 'version.py')).read())

setup(name=__package_name__,
      version=version_str,
      description='Linux networking unit-level testing',
      author=__author__,
      author_email=__email__,
      url='https://github.com/itayave/pynetest',
      license='GPLv3',
      platforms=['Linux'],
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      long_description=open(os.path.join(path, 'README.md'), 'r').read())
