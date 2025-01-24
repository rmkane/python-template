#!/usr/bin/env python3

import argparse
import datetime
import logging
import os

from pycli.utils.math import add_numbers, div_numbers, mul_numbers, sub_numbers

# Seup logging
logger = logging.getLogger(__name__)
log_dir = "logs"
today = datetime.datetime.now().strftime("%Y-%m-%d")
log_filename = f"{log_dir}/pycli_{today}.log"
os.makedirs(log_dir, exist_ok=True)


def add(args):
    logger.info(f"Adding {args.x} and {args.y}")
    result = add_numbers(args.x, args.y)
    print(f"The result of addition is: {result}")


def sub(args):
    logger.info(f"Subtracting {args.x} and {args.y}")
    result = sub_numbers(args.x, args.y)
    print(f"The result of subtraction is: {result}")


def mul(args):
    logger.info(f"Multiplying {args.x} and {args.y}")
    result = mul_numbers(args.x, args.y)
    print(f"The result of multiplication is: {result}")


def div(args):
    logger.info(f"Dividing {args.x} by {args.y}")
    if args.y != 0:
        result = div_numbers(args.x, args.y)
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")


def main():
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    parser = argparse.ArgumentParser(description="A simple CLI with subcommands")
    subparsers = parser.add_subparsers(
        title="subcommands", description="valid subcommands", help="additional help"
    )

    parser_add = subparsers.add_parser("add", help="Add two numbers")
    parser_add.add_argument("x", type=float, help="First number")
    parser_add.add_argument("y", type=float, help="Second number")
    parser_add.set_defaults(func=add)

    parser_sub = subparsers.add_parser("sub", help="Subtract two numbers")
    parser_sub.add_argument("x", type=float, help="First number")
    parser_sub.add_argument("y", type=float, help="Second number")
    parser_sub.set_defaults(func=sub)

    parser_mul = subparsers.add_parser("mul", help="Multiply two numbers")
    parser_mul.add_argument("x", type=float, help="First number")
    parser_mul.add_argument("y", type=float, help="Second number")
    parser_mul.set_defaults(func=mul)

    parser_div = subparsers.add_parser("div", help="Divide two numbers")
    parser_div.add_argument("x", type=float, help="First number")
    parser_div.add_argument("y", type=float, help="Second number")
    parser_div.set_defaults(func=div)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
