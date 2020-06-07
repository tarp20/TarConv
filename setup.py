"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['TarConv.py']
DATA_FILES = ['--iconfile']
OPTIONS = {'iconfile': '/Users/taras/Desktop/Projects/Conv/TarConv/cn.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)