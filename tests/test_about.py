#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Tests for metadata loading."""
import importlib
import pathlib
import runpy

import pytest


@pytest.fixture
def base_pkg():
    """Provide a reloaded base package as a fixture."""
    base_pkg = importlib.import_module("memoized_property")
    return importlib.reload(base_pkg)


@pytest.mark.parametrize(
    ["field", "value"],
    [
        ("distname", "memoized-property"),
        ("name", "memoized_property"),
        ("copyright", "Copyright (c) 2019 Rich Lewis"),
        ("license", "MIT license"),
        ("url", "https://lewisacidic.github.io/memoized-property"),
    ],
)
def test_metadata(base_pkg, field, value):
    """Test metadata is available on base package."""
    assert getattr(base_pkg, f"__{field}__") is not None


def test_version(base_pkg):
    """Test the version is correctly detected with versioneer."""
    versioneer_path = pathlib.Path(__file__).parents[1].joinpath("versioneer.py")
    versioneer = runpy.run_path(versioneer_path)
    version = versioneer["get_version"]()
    assert base_pkg.__version__ == version
