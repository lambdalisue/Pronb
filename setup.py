#!/usr/bin/env python
# vim: set fileencoding=utf8:
from setuptools import setup, find_packages

version = '0.0.0'

def read(filename):
    import os.path
    filename = os.path.join(os.path.dirname(__file__), filename)
    return open(filename).read()

setup(
    name="Pronb",
    version='0.0.0',
    description = "Internet notebook for programmer via Django",
    long_description=read('README.rst'),
    classifiers = [
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = "django notebook blog weblog",
    author = "Alisue",
    author_email = "lambdalisue@hashnote.net",
    url=r"https://github.com/lambdalisue/Pronb.git",
    download_url = r"https://github.com/lambdalisue/Pronb/tarball/master",
    packages = find_packages(exclude=['ez_setup']),
    include_package_data = True,
    zip_safe = False,
    test_suite='nose.collector',
    tests_require=['Nose'],
    install_requires=[
        'setuptools',
        'setuptools-git',
        'nose',
        'lettuce',
        'dateutils',
        'docutils',
        'pyyaml',
        'PIL',
        'django>=1.3',
        'django-qwert',
        'django-mfw',
    ],
)
