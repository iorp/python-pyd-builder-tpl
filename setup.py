 

from setuptools import setup
from Cython.Build import cythonize

setup(
    name='mylibrary',
    ext_modules=cythonize(['mylibrary/mylibrary.pyx']),
    packages=['mylibrary', 'mylibrary.mypackage1', 'mylibrary.mypackage2'],
    package_dir={'mylibrary': 'mylibrary'},
    zip_safe=False,
)