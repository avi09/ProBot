from setuptools import setup, find_packages

setup(
    name='ProBot',
    version='0.1',
    description=' ProBot is an interactive ChatBot to help with day to day tasks on general desktop and mobile environments.',
    author='agrawalavi',
    author_email='aagraw24@ncsu.edu',
    packages=find_packages(),
    tests_require=['pytest'],
      classifiers=[
          "License :: Apache License 2.0",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: ChatBot",
      ],

      license='Apache License 2.0',
      install_requires=[
        'yfinance',
        'nltk',
        'pandas',
        'kivy[full]'
      ]
)
