# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


version = '1.1.0'


setup(
    name='django-greenstalk',
    version=version,
    description='A convenience wrapper for beanstalkd clients and workers in Django using the greenstalk library for Python',
    long_description=open('README.md').read(),
    author='Stefan Klug',
    author_email='klug.stefan@gmx.de',
    url='https://github.com/beanstalkdclub/django-greenstalk',
    license='MPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyyaml',
        'greenstalk'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
