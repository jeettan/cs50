from setuptools import setup

APP=['lymphieapp.py']
DATA_FILES = ['background-le.png','logo.png', 'pic05.jpeg']

OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)