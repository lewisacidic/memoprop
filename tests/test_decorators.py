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
def tin(mock):
    """Delicious spam inside."""

    def inner(called=True, deletable=True, settable=True, classlevel=False):
        decorator = memoized_property(
            deletable=deletable, settable=settable, classlevel=classlevel
        )
        decorator = decorator if called else memoized_property

        class Spam(object):
            """Just some lovely spam."""

            @decorator
            def eggs(self):
                """Spammy method."""

                return mock()

        return Spam

    return inner


@pytest.mark.parametrize("called", [False, True])
def test_called(mock, tin, called):
    """Test default behaviour."""

    spam = tin(called=called)()
    assert spam.eggs == "yum"
    assert mock.call_count == 1
    assert spam.eggs == "yum"
    assert mock.call_count == 1


@pytest.mark.parametrize("deletable", [False, True])
def test_deletable(mock, tin, deletable):
    """Test deletable behaviour."""

    spam = tin(deletable=deletable)()
    condition = does_not_raise() if deletable else pytest.raises(AttributeError)

    assert spam.eggs == "yum"
    assert mock.call_count == 1

    with condition:
        del spam.eggs
        assert spam.eggs == "yum"
        assert mock.call_count == 2


@pytest.mark.parametrize("settable", [False, True])
def test_settable(mock, tin, settable):
    """Test settable behaviour."""

    spam = tin(settable=settable)()
    condition = does_not_raise() if settable else pytest.raises(AttributeError)

    assert spam.eggs == "yum"
    assert mock.call_count == 1

    with condition:
        spam.eggs = "yuck!"
        assert spam.eggs == "yuck!"
        assert mock.call_count == 1


@pytest.mark.parametrize("classlevel", [False, True])
def test_classlevel(mock, tin, classlevel):
    """Test class level behaviour."""

    Spam = tin(classlevel=True)  # noqa: N806
    spam1 = Spam()
    spam2 = Spam()

    assert spam1.eggs == "yum"
    assert mock.call_count == 1
    assert spam2.eggs == "yum"
    assert mock.call_count == 1 if classlevel else 2
