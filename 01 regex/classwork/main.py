"""
Classwork
"""

import re

# with open("seq.txt", "r") as file:
#     for line in file:
#         pattern = re.compile(r"(\w)\w*\s(\w+)")
#         res = pattern.sub(r"\2 \1.", line)
#         print(res, end="")

with open("f2.txt.utf", "r") as file:
    for line in file:
        res = re.search(r"(\((7|8)\)\d{10})", line)
        if res:
            print(res.group(1))
