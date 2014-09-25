#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 5
Task 01."""


def bool_to_str(bvalue, short = False):
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
    if bvalue == True and short == True:
        r = 'Y'
    elif bvalue == True and short == False:
        r = 'Yes'
    elif bvalue == False and short == True:
        r = 'N'
    else:
        r = 'No'
    return r
