try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='time-pretty-breaks',
    version='0.1',
    description='Split time, date and datetime intervals into '
    '"pretty" intervals',
    long_description=open('README.md').read(),
    author='Serhii Hulko',
    author_email='felytic@gmail.com',
    url='https://github.com/eos-vision/time_pretty_breaks',
    packages=['time_pretty_breaks'],
    install_requires=['python-dateutil'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
