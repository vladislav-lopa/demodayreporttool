from setuptools import find_packages
from setuptools import setup


setup(
    name='generate_report',
    version='0.3.0',
    packages=find_packages(),
    data_files=[('config', ['src/main/config.py'])],
    entry_points={
        'console_scripts': [
            'generate_report = src.reports.generate_html:Pages.generate_pages'
        ]
    },
    python_requires='>=3.9',
)