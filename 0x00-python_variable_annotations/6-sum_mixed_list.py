#!/usr/bin/env python3
"""This module return sum of mixed list"""
from typing import List, union


def sum_mixed_list(mxd_lst: List[union[float]]) -> float:
    """returns sum of mixed type of list"""

    return sum(mxd_lst)
