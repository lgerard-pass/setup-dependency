#!/usr/bin/python
import sys


def super_print(msg: str) -> None:
    print("SUUUUUUUUUPER PRIIIIIIIIIINT")
    print(msg)


if __name__ == "__main__":
    super_print(sys.argv[1])

