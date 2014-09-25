#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 5
Task 01."""
def bool_to_str(bvalue, short=False):
    """Returns a boolean as a string.

Args:
    bvalue(boolean, optional).
    short(bolean, Default : False).

Returns:
    string: Returns a string value of Yes/No/Y/N

Examples:
    >>> task_01.bool_to_str(False)
    'No'
    >>> task_01.bool_to_str(True, short=True)
    'Y'

"""
    if bvalue and short:
        rt = 'Y'
    elif bvalue and short is False:
        rt = 'Yes'
    elif bvalue is False and short:
        rt = 'N'
    else:
        rt = 'No'
    return rt
