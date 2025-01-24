#!/usr/bin/env python3

from pycli.utils.math import add_numbers, div_numbers, mul_numbers, sub_numbers

def test_add_numbers() -> None:
    assert add_numbers(1, 2) == 3

def test_sub_numbers() -> None:
    assert sub_numbers(2, 1) == 1

def test_mul_numbers() -> None:
    assert mul_numbers(2, 3) == 6

def test_div_numbers() -> None:
    assert div_numbers(6, 3) == 2.0
    assert div_numbers(6, 0) == float("inf")