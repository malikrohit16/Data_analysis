from setuptools import setup, find_packages

setup(
        name='data_analysis',
        version='0.0.1',
        url='www.github.com/malikrohit16/Data_analysis',
        license='',
        author='malikrohit16',
        packages=find_packages(),
        install_requires=['PyQt5',
                          'pandas',
                          'sqlalchemy',
                          'nltk',
                          'jupyter',
                          'python-twitter',],
        entry_point={},
        extras_require={'dev':['flake8']},
)
