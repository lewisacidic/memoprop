#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Define the project decorator."""
from functools import partial
from functools import wraps


def memoized_property(func=None, settable=False, deletable=True, classlevel=False):
    """Return the property attribute that only calls its getter on the first access.

    The result is cached as a private attribue of the same name as the property, and
    on subsequent accesses is returned, preventing the need to call the getter extra
    times.

    The decorator may be called in the same was as the builtin `property`, or
    providing options - see examples.

    Arguments:
        func: the getter function to be decorated.
        settable: whether to create a setter.
        deletable: whether to create a deleter.
        classlevel: whether to memoize at class level i.e. all instances share value.

    Examples:
        Use a decorator:
        >>> class DeepThought(object):
        ...     @memoized_property
        ...     def answer(self):
        ...         print("Running expensive getter...")
        ...         return 42

        >>> dt = DeepThought()

        Initially, the getter is called:
        >>> dt.answer
        Running expensive getter...
        42

        Subsequent accesses do not call the getter:
        >>> dt.answer
        42

        By default, a setter is not created:
        >>> dt.answer = 6 * 9
        Traceback (most recent call last):
            ...
        AttributeError: can't set attribute

        But a deleter is:
        >>> del dt.answer
        >>> dt.answer
        Running expensive getter...
        42

        The behaviours can be altered as follows:
        >>> class DeepThought(object):
        ...     @memoized_property(settable=True, deletable=False)
        ...     def answer(self):
        ...         print("Running expensive getter...")
        ...         return 42

        >>> dt = DeepThought()
        >>> dt.answer
        Running expensive getter...
        42

        >>> dt.answer = 6 * 9
        >>> dt.answer
        54

        >>> del dt.answer
        Traceback (most recent call last):
            ...
        AttributeError: can't delete attribute

        The memoization can be done at the class level
        >>> class DeepThought(object):
        ...     @memoized_property(classlevel=True)
        ...     def answer(self):
        ...         print("Running expensive getter...")
        ...         return 42

        >>> dt1, dt2 = DeepThought(), DeepThought()
        >>> dt1.answer
        Running expensive getter...
        42

        >>> dt2.answer
        42

        Of course, that means the property is only settable at class level:
        >>> class DeepThought(object):
        ...     @memoized_property(classlevel=True, settable=True)
        ...     def answer(self):
        ...         print("Running expensive getter...")
        ...         return 42

        >>> dt1, dt2 = DeepThought(), DeepThought()
        >>> dt1.answer = -1
        >>> dt1.answer
        -1

        >>> dt2.answer
        -1

    """

    if func is None:
        return partial(
            memoized_property,
            settable=settable,
            deletable=deletable,
            classlevel=classlevel,
        )

    attr_name = "_" + func.__name__

    lookup = type if classlevel else lambda x: x

    def fset(self, value):
        setattr(lookup(self), attr_name, value)

    def fdel(self):
        delattr(lookup(self), attr_name)

    @wraps(func)
    def fget(self):
        if not hasattr(self, attr_name):
            fset(self, func(self))
        return getattr(self, attr_name)

    return property(fget, fset if settable else None, fdel if deletable else None)
