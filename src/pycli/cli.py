#!/usr/bin/env python3

import logging
import os
from argparse import ArgumentParser, Namespace
from datetime import datetime

from pycli.utils.math import add_numbers, div_numbers, mul_numbers, sub_numbers


class AddCommand(Namespace):
    x: float = 0.0
    y: float = 0.0


class SubCommand(Namespace):
    x: float = 0.0
    y: float = 0.0


class MulCommand(Namespace):
    x: float = 0.0
    y: float = 0.0


class DivCommand(Namespace):
    x: float = 0.0
    y: float = 0.0


# Setup logging
logger = logging.getLogger(__name__)
log_dir = "logs"
today = datetime.now().strftime("%Y-%m-%d")
log_filename = f"{log_dir}/pycli_{today}.log"


def init_logging() -> None:
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def add(args: AddCommand) -> None:
    logger.info(f"Adding {args.x} and {args.y}")
    result = add_numbers(args.x, args.y)
    print(f"The result of addition is: {result}")


def sub(args: SubCommand) -> None:
    logger.info(f"Subtracting {args.x} and {args.y}")
    result = sub_numbers(args.x, args.y)
    print(f"The result of subtraction is: {result}")


def mul(args: MulCommand) -> None:
    logger.info(f"Multiplying {args.x} and {args.y}")
    result = mul_numbers(args.x, args.y)
    print(f"The result of multiplication is: {result}")


def div(args: DivCommand) -> None:
    logger.info(f"Dividing {args.x} by {args.y}")
    if args.y != 0:
        result = div_numbers(args.x, args.y)
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")


def init_parser() -> tuple[ArgumentParser, Namespace]:
    parser = ArgumentParser(description="A simple CLI with subcommands")
    subparsers = parser.add_subparsers(
        title="subcommands",
        description="valid subcommands",
        help="additional help",
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

    return parser, args


def main() -> None:
    parser, args = init_parser()

    if hasattr(args, "func"):
        init_logging()
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
