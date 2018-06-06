from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'LICENSE')) as f:
    license = f.read()

setup(name='sample',
      version='0.1',
      description='Sample project for data engineer',
      long_description = long_description,
      url='https://github.com/kd2926/sampleproject',
      author='LetsDoThis',
      author_email='letsdothis2926@gmail.com',
      license=license,
      packages=find_packages(),
      scripts=['sample/fever_count_per_day_zip.py'],
      install_requires= [ 'pandas'],
      zip_safe=False)

