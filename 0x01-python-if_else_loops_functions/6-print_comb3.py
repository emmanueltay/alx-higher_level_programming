#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (not((j == i) or (i > j))):
            print("{}{}".format(i, j), end="")
            if (not(j == 9 and i == 8)):
                print("{}".format(', '), end="")
print()
