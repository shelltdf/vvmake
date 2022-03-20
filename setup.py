#!usrbinenv python

import re
import setuptools

version = "0.3.0"
# with open('vvmake/__init__.py', 'r') as fd:
    # version = re.search(r"^__version__s=s[']([^'])[']",
                        # fd.read(), re.MULTILINE).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vvmake",
    version=version,
    author="will",
    author_email="shell_tdf@126.com",
    description="This is the SDK for example.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://example.com",
    entry_points = {'console_scripts': ['vvmake=vvmake:main'] },
    package_dir = {'': 'vvmakelib'},
    # install_requires=[
        # 'requests!=2.9.0',
        # 'lxml=4.2.3',
        # 'monotonic=1.5',
    # ],
    # packages=setuptools.find_packages(exclude=("test")),
    # classifiers=(
        # "License  OSI Approved  MIT License",
        # "Intended Audience  Developers",
        # "Operating System  OS Independent",
        # "Programming Language  Python",
        # "Programming Language  Python  2",
        # "Programming Language  Python  2.6",
        # "Programming Language  Python  2.7",
        # "Programming Language  Python  3",
        # "Programming Language  Python  3.3",
        # "Programming Language  Python  3.4",
        # "Programming Language  Python  3.5"
    # ),
    # exclude_package_data={'' ,["vmake/test.py", "vmake/config.txt"]},
)

