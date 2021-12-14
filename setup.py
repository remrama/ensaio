# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Setup configuration for the Python package.

Metadata and build configuration are defined in setup.cfg
Uses setuptools-scm to manage version numbers using git tags.
"""
from setuptools import setup

if __name__ == "__main__":
    setup(
        use_scm_version={
            "relative_to": __file__,
            "version_scheme": "post-release",
            "local_scheme": "node-and-date",
            "write_to": "ensaio/_version_generated.py",
        }
    )
