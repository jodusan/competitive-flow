#!/usr/bin/python3

# --------------------------------------------------------------------------- #
# This script allows you to quickly run all test cases that are saved within
# your source file as JSON object. Best way to do this is to use cf-paste
# script.
#
# https://github.com/dulex123/backpack/tree/master/cf-meta
# --------------------------------------------------------------------------- #
import re
import json
import sys
import os
import subprocess
from subprocess import PIPE, TimeoutExpired
from collections import OrderedDict as oDict

# Shell status colors
OK_GREEN = ''
FAIL = ''
if os.name != 'nt':
	OK_GREEN = '\033[92m'
	FAIL = '\033[91m'


# Current directory of invoked script
cwd = os.getcwd() + '/'

if len(sys.argv) != 2:
    print(FAIL + "Error: Argument missing")
    sys.exit()

# Name of source file
src = ""
if sys.argv[1].endswith(".cpp"):
    src = sys.argv[1]
else:
    src = sys.argv[1] + ".cpp"

exe = src[:-4]

# Check if file exists
if not os.path.isfile(src):
    if not os.path.isfile(exe):
        print(FAIL + "Error: Source file doesn't exist")
        sys.exit()
    else:
        src = exe

# Read source file as string
data = open(src, 'r').read()

# Search for pattern of comment-enclosed /*JSON object*/
pattern = r'/\*\s({.*})\s\*/'  # r - RAW string, because python strings :')

# Find the matching sequence, json object is within first group
# re.M - Multi-line matching
# re.S - Make . match any character including newlines
match = re.search(pattern, data, re.M | re.S)
if not match:
    print (FAIL + "Error: No tests found in file!")
    sys.exit()
json_data = match.group(1)

# Convert to dictionary from json
info = json.loads(json_data, object_pairs_hook=oDict)

# Create /tmp/competitive dir
os.makedirs("/tmp/competitive/", exist_ok=True)
os.chdir("/tmp/competitive")

# Compile our program
status = subprocess.Popen(["g++", "-o", exe, cwd + src, "-std=c++11"]).wait()
if status != 0:
    print("Error: Compiler had a problem.")
    sys.exit()

# Foreach test run program
for test, val in info["tests"].items():
    proc = subprocess.Popen(["./" + exe],
                            stdout=PIPE,
                            stdin=PIPE,
                            stderr=PIPE,
                            universal_newlines=True)
    try:
        outs, errs = proc.communicate(input=val["in"], timeout=15)
    except TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
    outs_comp = outs.replace('\n', ' ').strip()


    if outs_comp == val["out"]:
        print(OK_GREEN + test + " - " + "OK")
    else:
        print(FAIL + test + " - FAIL")
        print(val["out"])
        print(outs)