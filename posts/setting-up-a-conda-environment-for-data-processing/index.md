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

We are using the [anaconda]() Python distribution to install the libraries we need and manage our different computing environments. Here I want to share some tips: 

+ A good idea is to **never** mix in the same environment libraries sourced from the *default* conda channel and *conda-forge*. I have battled in the past with broken environments, especially when trying to install geospatial python packages (such as geopandas, rasterio, shapely, gdal, etc) exactly for that reason. For a working 'geospatial' environment I found the best is to install *everything* from conda-forge (including the foundational packages such as Numpy, Scipy, Pandas etc)

+ The latest version of [xarray]() (Version 0.11) now can read grib files using [cfgrib](). cfgrib itself depends on [eccodes]() which is available on the conda-forge channel. So if you do: 

  ```
  conda install -c conda-forge eccodes 
  pip install cfgrib 
  ```

  you should be good to go. 

  If xarray + cfgrib somehow doesnt read your grib files, there's a good chance [pygrib]() will, again you are in luck as it is available on the *conda-forge* channel, so `conda install -c conda-forge pygrib` will install pygrib, and you now have two options for reading your grib files. 