from setuptools import find_packages, setup

setup(
    name='ml_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit_learn',
        'matplotlib',
        'seaborn',
        'joblib'
    ],
)