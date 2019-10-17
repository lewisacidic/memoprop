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


BASEDIR = pathlib.Path(__file__).parents[1]


@pytest.fixture
def base_pkg():
    """Provide a reloaded base package as a fixture."""
    base_pkg = importlib.import_module("memoprop")
    return importlib.reload(base_pkg)


@pytest.mark.parametrize(
    ["field", "value"],
    [
        ("distname", "memoprop"),
        ("name", "memoprop"),
        ("copyright", "Copyright (c) 2019 Rich Lewis"),
        ("license", "MIT license"),
        ("url", "https://lewisacidic.github.io/memoprop"),
    ],
)
def test_metadata(base_pkg, field, value):
    """Test metadata is available on base package."""
    assert getattr(base_pkg, f"__{field}__") is not None


def test_version(base_pkg):
    """Test the version is correctly detected with versioneer."""
    # get versioneer.py version
    versioneer_path = str(BASEDIR.joinpath("versioneer.py"))
    versioneer = runpy.run_path(versioneer_path)
    version = versioneer["get_version"]()
    assert base_pkg.__version__ == version


def test_import_fails():
    """Test behavior if import fails."""
    # if we run __about__ as a script with runpy, imports fail as planned in setup.py
    about_path = str(BASEDIR.joinpath("src", "memoprop", "__about__.py"))
    about = runpy.run_path(about_path)
    assert about["__version__"] is None
