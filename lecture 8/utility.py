"""utility.py
"""
from typing import List


def matrix_mult(A, B):
    temp_b = zip(*B)
    return [[sum(ea * eb for ea, eb in zip(a, b)) for b in temp_b] for a in A]


def cleanup_list(nums: List[float], places=5):
    return [round(num, places) for num in nums]
