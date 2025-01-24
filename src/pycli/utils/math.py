#!/usr/bin/env python3


def add_numbers(a: float, b: float) -> float:
    return a + b


def sub_numbers(a: float, b: float) -> float:
    return a - b


def mul_numbers(a: float, b: float) -> float:
    return a * b


def div_numbers(a: float, b: float) -> float:
    return a / b if b != 0 else float("inf")
