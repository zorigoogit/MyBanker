from setuptools import setup, find_packages

setup(
    name='MyBanker',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=['MyBanker_Main', 'AccountServices'],
    author='Munkhzorig',
    author_email='munkhzorig.ts@gmail.com',
    description='Simple banking console application.',
    install_requires=[
        # dependencies
    ],
    entry_points={
        'console_scripts': [
            'MyBanker = MyBanker_Main:main',
        ],
    },
)