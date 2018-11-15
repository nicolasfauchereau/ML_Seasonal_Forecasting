<!--
.. title: Setting up a conda environment for data processing
.. slug: setting-up-a-conda-environment-for-data-processing
.. date: 2018-11-15 17:34:28 UTC+13:00
.. tags: conda, grib
.. category: 
.. link: 
.. description: 
.. type: text
-->

We are using the [anaconda](http://www.anaconda.com) Python distribution to install the libraries we need and manage our different computing environments. Here I want to share some tips: 

+ A good idea is to **never** mix in the same environment libraries sourced from the *default* conda channel and *conda-forge*. I have battled in the past with broken environments, especially when trying to install geospatial python packages (such as geopandas, rasterio, shapely, gdal, etc) exactly for that reason. For a working 'geospatial' environment I found the best is to install *everything* from conda-forge (including the foundational packages such as Numpy, Scipy, Pandas etc)

+ The latest version of [xarray]() (Version 0.11) now can read grib files using [cfgrib](). cfgrib itself depends on [eccodes]() which is available on the conda-forge channel. So if you do: 

  ```python
  conda install -c conda-forge eccodes   
  ```

  Then

  ```python
  pip install cfgrib   
  ```

  you should be good to go. 

  If xarray + cfgrib somehow doesn't read your grib files, there's a good chance [pygrib](https://github.com/jswhit/pygrib), written by [Jeffrey Whitaker](https://www.esrl.noaa.gov/psd/people/jeffrey.s.whitaker/) will. Again you are in luck as it is available on the *conda-forge* channel, so `conda install -c conda-forge pygrib` will install pygrib, and you now have two options for reading your grib files. 

----

Below is the list of library we'll be using during the course of the project for all the data management and data processing tasks (i.e. excluding the Machine Learning aspect *per-se*): 

+ [xarray](http://xarray.pydata.org) 
+ [intake](https://intake.readthedocs.io/en/latest/quickstart.html) and [intake-xarray](https://github.com/ContinuumIO/intake-xarray)
+ [pygrib](https://github.com/jswhit/pygrib) to read datasets available in grib format
+ [cfgrib](https://github.com/ecmwf/cfgrib) same thing ... 
+ [cdsapi](https://pypi.org/project/cdsapi/) to download the seasonal forecasts made available on the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu)