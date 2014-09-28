#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides loan management features."""

import decimal

#interval = 12
#rate = None
#total = None

def get_interest_rate(principal, duration, prequalification):
    if principal >= 0 and principal <= 199999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0363'
            else:
                rate = '0.0465'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0404'
            else:
                rate = '0.0498'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0577'
            else:
                rate = '0.0639'
    elif principal >= 200000 and principal <= 999999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0302'
            else:
                rate = '0.0398'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0327'
            else:
                rate = '0.0408'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0466'
    elif principal >= 1000000:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0205'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0262'
    rate = decimal.Decimal(rate)
    return rate

def compound_interest(principal, duration, rate, interval = 12):
    if rate is not None:
        rate = decimal.Decimal(rate)
        compound = principal * ((1 + rate / interval) ** (interval * duration))
    else: compound = None
    return decimal.Decimal(compound)

def calculate_total(principal, duration, prequalification):
    rate = None
    get_interest_rate(principal, duration, prequalification)                                                                                                                                                                                                                                                                                                                                                                                                                            
    return  rate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
