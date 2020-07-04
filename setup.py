from setuptools import setup
import re


def get_version():
    f = open('flake8_simplicity.py')
    try:
        for line in f:
            m = re.match(r'__version__ = [\'"](.*)[\'"]\s*$', line)
            if m:
                return m[1]

        return '0.0.0'
    finally:
        f.close()


def get_long_description():
    f = open('README.md')
    try:
        return f.read()
    finally:
        f.close()


setup(
    name='flake8-simplicity',
    version=get_version(),
    description='Take your Python syntax back to the 90s!',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    keywords='flake8 simplicity __past__',
    author='James Haggerty',
    author_email='james.haggerty@gmail.com',
    url='https://github.com/wryun/flake8-simplicity',
    license='MIT',
    py_modules=['flake8_simplicity'],
    entry_points={
        'flake8.extension': [
            'SPL = flake8_simplicity:checker',
        ],
    },
    install_requires=['flake8 > 3.0.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flake8',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
