import os, sys
import setuptools
from setuptools import find_packages

os.system("cp server_config.yaml ppulse/")

if "--client_only" in sys.argv:
    install_list = ['ppulse']
    cli_list = {
        "console_scripts": [
            "ppulse = ppulse.cli:ppulse",
        ]
    }
    sys.argv.remove("--client_only")
else:
    install_list = ['ppulse','ppulseserver']
    cli_list = {
        "console_scripts": [
            "ppulse = ppulse.cli:ppulse",
            "ppulseserver = ppulseserver.cli:ppulseserver",
        ]
    }

setuptools.setup(
    name="ppulse",
    version="0.0.1",
    packages=install_list,
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
    entry_points=cli_list,
    include_package_data=True,
    package_data = {
        '': ['*.yaml']
    },
)