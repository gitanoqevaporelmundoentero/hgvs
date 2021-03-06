#!/usr/bin/env python

from setuptools import setup
from pip.req import parse_requirements
import sys

description = ("This library provides a simple to use Python API for parsing, "
               "formatting, and normalizing variant names specified in the "
               "standard recommended by the Human Genome Variation Society "
               "(HGVS).")


def main():
    python_version = sys.version_info
    if python_version < (2, 6):
        print ("This library requires Python version >=2.6, "
               "You have version %d.%d" % python_version[:2])
        sys.exit(1)

    setup(
        name='hgvs',
        version='0.8',
        description='HGVS name parsing and formatting',
        long_description=description,
        author='Matt Rasmussen',
        author_email='rasmus@counsyl.com',
        packages=['hgvs', 'hgvs.tests'],
        scripts=[],
        tests_require=[str(line.req) for line in
                       parse_requirements('requirements-dev.txt')],
        setup_requires=['nose==1.3.0'],
    )

if __name__ == '__main__':
    main()
