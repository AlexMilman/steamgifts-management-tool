
# Utilities for working with strings
# Copyright (C) 2017  Alex Milman

def normalize_float(float_str):
    return float(float_str.replace(',', ''))


def normalize_int(int_str):
    return int(int_str.replace(',', ''))
