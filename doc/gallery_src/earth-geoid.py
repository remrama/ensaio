# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Earth geoid height grid at 10 arc-minute resolution
---------------------------------------------------

The grid is grid-node registered and stored in netCDF with CF-compliant
metadata. The geoid height is derived from the EIGEN-6C4 spherical harmonic
model of the Earth's gravity field.

**Original source:** `EIGEN-6C4 model
<https://doi.org/10.5880/icgem.2015.1>`__

**Pre-processing:** `Source code for preparation of the original dataset for
redistribution in Ensaio
<https://github.com/fatiando-data/earth-geoid-10arcmin>`__
"""
import pygmt
import xarray as xr

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk.
fname = ensaio.fetch_earth_geoid(version=1)
print(fname)

###############################################################################
# Load the netCDF grid with xarray.
data = xr.load_dataarray(fname)
data

###############################################################################
# Make a PyGMT pseudo-color map of the grid in a Mollweide projection.
fig = pygmt.Figure()
fig.basemap(
    region="g",
    projection="W15c",
    frame=True,
)
fig.grdimage(data, cmap="polar+h")
fig.colorbar(frame='af+l"geoid height [m]"')
fig.coast(shorelines=True, resolution="c", area_thresh=1e4)
fig.show()
