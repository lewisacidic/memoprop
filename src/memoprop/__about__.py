#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Metadata for memoprop."""
# guard import
# in setup.py we use run this with runpy so the import will fail
try:
    from ._version import get_versions

    __version__ = get_versions()["version"]
    del get_versions
except ImportError:
    __version__ = None

__distname__ = "memoprop"
__name__ = "memoprop"
__description__ = "Basic memoized properties for Python."
__license__ = "MIT license"
__copyright__ = "Copyright (c) 2019 Rich Lewis"

__author__ = "Rich Lewis"
__author_email__ = "opensource@richlew.is"

__url__ = "https://lewisacidic.github.io/memoprop"
__docs_url__ = "https://lewisacidic.github.io/memoprop/docs"
__source_url__ = "https://github.com/lewisacidic/memoprop"
__bugtracker_url__ = "https://github.com/lewisacidic/memoprop/issues"
__download_url__ = "https://github.com/lewisacidic/memoprop/releases"

__classifiers__ = [
    "Development Status :: 2 - Pre-Alpha",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Natural Language :: English",
]

__keywords__ = ["decorator", "property", "memoized"]

__all__ = [
    "__author__",
    "__author_email__",
    "__bugtracker_url__",
    "__classifiers__",
    "__copyright__",
    "__description__",
    "__distname__",
    "__docs_url__",
    "__download_url__",
    "__keywords__",
    "__license__",
    "__name__",
    "__source_url__",
    "__url__",
    "__version__",
]
