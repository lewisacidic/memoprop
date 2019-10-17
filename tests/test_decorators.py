#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Tests for base memoized decorator."""
from contextlib import ExitStack as does_not_raise  # noqa: N813

import pytest
from memoprop import memoized_property


@pytest.fixture
def mock(mocker):
    """A tasty mock."""

    return mocker.Mock(return_value="yum")


@pytest.fixture
def spam(mock, called, deletable, settable):
    """Makes spam."""

    dec = (
        memoized_property(deletable=deletable, settable=settable)
        if called
        else memoized_property
    )

    class Spam(object):
        """Just some lovely spam."""

        @dec
        def eggs(self):
            """Spammy method."""

            return mock()

    return Spam()


@pytest.mark.parametrize("deletable", [True])
@pytest.mark.parametrize("settable", [False])
@pytest.mark.parametrize("called", [False, True])
def test_called(mock, spam, called, deletable, settable):
    """Test default behaviour."""

    assert spam.eggs == "yum"
    assert mock.call_count == 1
    assert spam.eggs == "yum"
    assert mock.call_count == 1


@pytest.mark.parametrize("called", [True])
@pytest.mark.parametrize("settable", [False])
@pytest.mark.parametrize("deletable", [False, True])
def test_deletable(mock, spam, called, deletable, settable):
    """Test deletable behaviour."""
    condition = does_not_raise() if deletable else pytest.raises(AttributeError)

    assert spam.eggs == "yum"
    assert mock.call_count == 1

    with condition:
        del spam.eggs
        assert spam.eggs == "yum"
        assert mock.call_count == 2


@pytest.mark.parametrize("called", [True])
@pytest.mark.parametrize("deletable", [True])
@pytest.mark.parametrize("settable", [False, True])
def test_settable(mock, spam, called, deletable, settable):
    """Test setable behaviour."""
    condition = does_not_raise() if settable else pytest.raises(AttributeError)

    assert spam.eggs == "yum"
    assert mock.call_count == 1

    with condition:
        spam.eggs = "yuck!"
        assert spam.eggs == "yuck!"
        assert mock.call_count == 1
