#!/usr/bin/env python3


import sys
import re


def my_printf(format_string, param):
    match = re.search("#(\.\d+)?k", format_string)

    if not match:
        print(format_string)
        return

    replacement = format_string[match.start() : match.end()]

    max_chars = len(param)
    if match.group(1):
        max_chars = int(match.group(1)[1:])

    print(format_string.replace(replacement, param.swapcase()[:min(len(param), max_chars)]))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
