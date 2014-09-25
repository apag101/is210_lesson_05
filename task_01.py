#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 5
Task 01."""


def bool_to_str(bvalue, short == False):
    """Returns a boolean as a string.

    Args:
        bool_to_string(bvalue): Boolean value of True or False.
		bool_to_string(short): Short value of Y or N, for bvalue.

	Defaults:
		bool_to_string(short): Default value of false.

    Returns:
        string: Returns a string value of Yes/No/Y/N

    Examples:
        >>> task_01.bool_to_str(False)
        'No'
        >>> task_01.bool_to_str(True, short=True)
        'Y'

    """
    if bvalue == True and short == True:
        return 'Y'
    elif bvalue == True and short == False:
        return 'Yes'
    elif bvalue == False and short == True:
        return 'N'
    else:
        return 'No'
