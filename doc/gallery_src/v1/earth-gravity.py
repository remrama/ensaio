# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Gravity of the Earth at 10 arc-minute resolution
------------------------------------------------

The grid is grid-node registered and stored in netCDF with CF-compliant
metadata. The gravity values are derived from the EIGEN-6C4 spherical harmonic
model. Here "gravity" refers to the combined gravitational and centrifugal
accelerations.

The data are calculated uniformly at 10 km above the WGS84 ellipsoid.

**Original source:** `EIGEN-6C4 model
<https://doi.org/10.5880/icgem.2015.1>`__

"""
import xarray as xr
import pygmt

import ensaio.v1 as ensaio

###############################################################################
# Download and cache the data and return the path to it on disk.
fname = ensaio.fetch_earth_gravity()
print(fname)

###############################################################################
# Load the netCDF grid with xarray.
#
# .. note::
#
#     Requires the `netcdf4 <https://github.com/Unidata/netcdf4-python>`__
#     library.
#
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
fig.grdimage(data, cmap="viridis", shading="+nt0.5")
fig.colorbar(frame='af+l"gravity [mGal]"')
fig.coast(shorelines=True, resolution="c", area_thresh=1e4)
fig.show()
