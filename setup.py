from setuptools import setup

setup(
    name='rippling_cli',
    version='0.1.0',
    packages=['rippling_cli'],
    entry_points={
        'console_scripts': [
            'rippling-cli=rippling_cli.cli.main'
        ]
    })
