# python setup.py build
from distutils.core import setup, Extension

mymodule = Extension('mymodule', sources = ['mymodule.cpp'])

setup(
    name        = 'mymodule',
    version     = '1.0',
    description = 'Sample python C-API exploration',
    ext_modules = [mymodule]
)
