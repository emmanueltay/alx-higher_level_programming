#!/usr/bin/python3
if _name_ == "_main_":
    import sys

result = 0
for i in range(len(sys.argv) - 1):
    result += int(sys.argv[i + 1])

print("{}".format(result))
