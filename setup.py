from setuptools import setup, find_packages
from version import find_version

setup(
        name = 'conversion_metrics',
        author = 'Jiaxiang Li',
        description = 'calculate and visualize conversion rates and related metrics',
        license = 'MIT',
        version = find_version('conversion_metrics', '__init__.py'),
        packages = find_packages()
     )
