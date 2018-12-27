from setuptools import setup, find_packages


setup(
    name='slapdash',
    version='0.1',
    py_modules=['slapdash'],
    install_requires=[
        'dash>0.26.1',
        'dash-html-components',
        'dash-core-components',
        'dash-bootstrap-components',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
