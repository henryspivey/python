#!/usr/bin/env python
import sys
import re
import os
# get the start directory
start =sys.argv[1]

# get the patterns from the command line arguments
pattern = sys.argv[2]

#convert them to regexs
expr = re.compile(pattern)

# traverse the directories for all files
for root,dirs, files in os.walk(start):
    for fname in files:
        if expr.match(fname):
            print(root, fname)