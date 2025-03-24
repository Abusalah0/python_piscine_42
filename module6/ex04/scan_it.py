#!/usr/bin/python3

import sys
import re

if (len(sys.argv) != 3):
    print('none')
else:
    occu = re.findall(sys.argv[1], sys.argv[2])
    if (len(occu) == 0):
        print('none')
    else:
        print(len(occu))
