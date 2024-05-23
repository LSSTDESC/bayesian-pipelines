from setuptools import find_packages, setup

setup(
    name="bpp",
    version="0.0.1",
    url="https://github.com/LSSTDESC/bayesian-pipelines-pixels",
    author="Ismael Mendoza",
    author_email="imendoza@umich.edu",
    description="Bayesian Pixel Pipeline for LSST",
    packages=find_packages(),
    install_requires=["numpy", "jax", "galsim"],
)
