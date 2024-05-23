# Bayesian Pixel Pipeline

Bayesian inference of lensing shear directly from pixels.

This project aims to demonstrate probabilistic analysis of simulated Rubin single-visit and coadd images to infer posterior weak lensing shear and convergence fields on the sky. The modeling will be tested on both forward simulated data and LSST DESC Data Challenge 2 (DC2) images.

We are building a Bayesian pipeline for weak lensing shear and convergence inference combining multiple existing DESC tools/projects. Our pipeline includes a generative model for galaxy images that is used for inference as well as training and validation of specific inference algorithms. The generative model starts from a fixed cosmology and redshift distribution, uses two-dimensional random (Gaussian or log-Normal) fields to build a correlated shear field, and uses `galsim` to draw and shear galaxies. The inference pipeline will consist of detection, deblending, shape inference, and shear inference stages.

See the [Project Roadmap](https://github.com/LSSTDESC/bayesian-pipelines-pixels/issues/54) for details about the structure of the generative model and inference pipeline.


## Install

```bash
# fresh conda env
pip install --upgrade pip
conda create -n bpp python=3.10
conda activate bpp

# Install JAX
pip install --upgrade "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

# descwl-shear-sims dependencies
conda install -c conda-forge mamba
mamba install -c conda-forge stackvana
mamba install -c conda-forge pip lsstdesc.weaklensingdeblending numba galsim ipykernel ngmix matplotlib

pip install git+https://github.com/LSSTDESC/descwl-shear-sims.git
pip install git+https://github.com/esheldon/metadetect.git
pip install git+https://github.com/GalSim-developers/JAX-GalSim.git

pip install numpyro h5py ChainConsumer numpy galcheat
pip install black flake8 isort ipython pytest


cd bayesian-pipelines-pixels
pip install -e .
```
