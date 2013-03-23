#-*- coding:utf-8 -*-

import setuptools
import sphinx_tweet_embed as pkg

pkgname = pkg.__name__

setuptools.setup(
    name=pkgname,
    version=pkg.__version__,
    packages=[pkgname],
    install_requires=[
        'sphinx'
        ],
    author=pkg.__author__,
    license=pkg.__license__,
    url='https://github.com/shomah4a/sphinx-tweet-embed',
    description='''embedding twitter's tweet in sphinx''',
    long_description=pkg.__doc__,
    classifiers='''
Programming Language :: Python
Development Status :: 2 - Pore-Alpha
License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Topic :: Software Development :: Documentation
'''.strip().splitlines())

