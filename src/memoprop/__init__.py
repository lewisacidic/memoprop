#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Define properties which cache the result of their getter.

See `memoprop.__about__` for more info.
"""
from .__about__ import __copyright__
from .__about__ import __distname__
from .__about__ import __license__
from .__about__ import __url__
from .__about__ import __version__
from .decorators import memoized_property

__all__ = [
    "__copyright__",
    "__distname__",
    "__license__",
    "__url__",
    "__version__",
    "memoized_property",
]
