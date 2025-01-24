#!/usr/bin/env python3


def add_numbers(a: int, b: int) -> int:
    return a + b


def sub_numbers(a: int, b: int) -> int:
    return a - b


def mul_numbers(a: int, b: int) -> int:
    return a * b


def div_numbers(a: int, b: int) -> float:
    return a / b if b != 0 else float("inf")
