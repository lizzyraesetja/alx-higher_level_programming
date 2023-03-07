#!/usr/bin/python3
for l in range(ord('a'), ord('z') + 1):
    if l != ord('q') and l != ord('e'):
        print("{:s}".format(chr(l)), end="")
