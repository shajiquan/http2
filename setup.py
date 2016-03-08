#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='http2',
    version='0.2.1',
    description="HTTP/2 client with hyper-h2 for tornado",
    author="boyxuper",
    author_email='boyxuper@gmail.com',
    url='https://github.com/mSOHU/http2',
    packages=[
        'http2',
    ],
    package_dir={
        'http2': 'http2',
    },
    install_requires=[
        'h2>=2.1.0',
        'tornado>=2.4.1',
        'backports.ssl_match_hostname',
    ],
    license="Apache Software License",
    zip_safe=False,
    keywords='http2 tornado',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
