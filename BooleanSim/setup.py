import os
from setuptools import setup

#def read(fname):
#    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "BooleanSim",
    version = "0.1",
    author = "Je-Hoon Song",
    author_email = "song.jehoon@gmail.com",
    description = ( "A simulator for boolean network"),
    license = "BSD",
    keywords = "boolean network simulator",
    url = "",
    packages=['boolean3', 'boolean3_addon', 'boolean3/plde', 'boolean3/ply'],
    long_description='boolean simulation program',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
