import os
import sys

from setuptools import setup, find_packages
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from config.version import Version as ver

version = ver(Dir=True).version


def strip_comments(path):
    return path.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(path) for path in open(os.path.join(os.getcwd(), *f)).readlines()]))


setup(
    name='CustomLibrary',
    version=version,
    author='Xinertel',
    author_email='support@xinertel.com',
    description='Custom Library.',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: windows Linux',
        'Programming Language :: Python :: 3',
    ],
    install_requires=reqs('requirements-custom.txt'),
    packages=find_packages(include=["CustomLibrary", "NtoLibrary", "config"])
)
