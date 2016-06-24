
from setuptools import setup

setup(name='email_format',
      version='1.0',
      description='Wrapper around zlib with custom header crc32.',
      url='http://github.com/killswitch-GUI/zlib_format',
      author='Alexander Rymdeko-Harvey',
      author_email='lolyearight@cybersyndicates.com',
      license='GNU 3.0',
      packages=['zlib_wrapper'],
      install_requires=[
          'zlib',
      ],
      zip_safe=False)
