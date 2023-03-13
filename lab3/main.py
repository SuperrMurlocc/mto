#!/usr/bin/env python3

import re
import sys

def my_printf(format_string,param):
    match = re.search(r'#([1-9]\d*)?(\.\d+)?k', format_string)

    if not match:
        print(format_string)
        return

    replacement = match.group(0)

    param = param.swapcase()

    print(format_string.replace(replacement, param))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
