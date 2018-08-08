from setuptools import setup, find_packages


setup(
    name='slapdash',
    version='0.1',
    py_modules=['slapdash'],
    install_requires=[
        # TODO: add minimum version requirements
        'dash',
        'dash-renderer',
        'dash-html-components',
        'dash-core-components',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
