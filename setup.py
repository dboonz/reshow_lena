#!/usr/bin/env python

from setuptools import setup

def read_file(filename):
    with open(filename) as f:
        x = f.readlines()
    return x


setup(name='reshow_lena',
            version='0.1',
            description=read_file('description.md'),
            author='Dirk Boonzajer',
            author_email='dboonz@gmail.com',
            packages=['reshow_lena'],
           )
