#!/usr/bin/python3
# --------------------------------------------------------------------------- #
# This script allows you to quickly paste test examples for codeforces problems
# within your source file as JSON object. It is designed to be used alongside
# cf-tool that allows you to quickly test all test cases.
#
# https://github.com/dulex123/backpack/tree/master/cf-meta
# --------------------------------------------------------------------------- #

import json
import pyperclip
from collections import OrderedDict as oDict

# Our json object that will contain all data about our source code
json_out = oDict()
json_out["name"] = ""
json_out["desc"] = ""
json_out["tags"] = ""
json_out["tests"] = oDict()

# Get content from clipboard
data = pyperclip.paste()

# Arrays for inputs/outputs of test cases
in_array = []
out_array = []

in_temp = ""
out_temp = ""

# Get all inputs/outputs
flag_in = True
flag_out = False
for line in data.splitlines()[1:]:
    if line == "Input" or line == "input":
        flag_in = True
        flag_out = False
        out_array.append(out_temp.strip())
        out_temp = ""
    elif line == "Output" or line == "output":
        flag_in = False
        flag_out = True
        in_array.append(in_temp.strip())
        in_temp = ""
    elif line == "":
        continue
    elif flag_in:
        in_temp += line.replace('\n', ' ') + ' '
    elif flag_out:
        out_temp += line.replace('\n', ' ') + ' '
out_array.append(out_temp.strip())

i = 0
for test_in, test_out in zip(in_array, out_array):
    i += 1
    json_out["tests"]["test" + str(i)] = oDict()
    json_out["tests"]["test" + str(i)]["in"] = test_in
    json_out["tests"]["test" + str(i)]["out"] = test_out

# Save to clipboard as c++ commented JSON object
clipboard_content = "/*\n" + json.dumps(json_out, indent=4) + "\n*/"
pyperclip.copy(clipboard_content)
