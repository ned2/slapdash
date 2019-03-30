from setuptools import setup, find_packages


setup(
    name="slapdash",
    version="0.1",
    py_modules=["slapdash"],
    install_requires=["dash>=0.40.0", "dash-bootstrap-components>=0.3.0"],
    packages=find_packages("src"),
    package_dir={"": "src"},
)
