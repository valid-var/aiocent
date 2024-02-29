import os
import sys
from setuptools import setup


if sys.argv[-1] == 'test':
    status = os.system('python tests/tests.py')
    sys.exit(1 if status > 127 else status)


requirements = ['aiohttp']


def long_description():
    return "Async Python library to communicate with Centrifugo v3 HTTP API, fork of pycent package"


setup(
    name='aiocent',
    version='4.1.0',
    description="Async Python library to communicate with Centrifugo v3 HTTP API, fork of pycent package",
    long_description=long_description(),
    url='https://github.com/valid_var/aiocent',
    download_url='https://github.com/valid_var/aiocent',
    author="Stepan Starovoitov",
    author_email='stepan.startech@gmail.com',
    license='MIT',
    packages=['aiocent'],
    entry_points={
        'console_scripts': [
            'aiocent = aiocent.console:run',
        ],
    },
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ]
)
