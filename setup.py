import os
import setuptools
from setuptools import find_packages


setuptools.setup(
    name="ppulse",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'click==8.1.3',
        'requests==2.27.1',
        'PyYAML>=6.0',
        'Flask>=2.3.2',
        'waitress>=2.1.2'
    ],
    description="Manage 2x2 LED pulser",
    author="Livio Calivers, University of Bern",
    classifiers=["Intended Audience :: Information Technology",
                 "Operating System :: POSIX :: Linux",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.6"],
    entry_points={
        "console_scripts": [
            "ppulse = ppulse.cli:ppulse",
        ]
    },
)
