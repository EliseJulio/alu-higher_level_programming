#!/usr/bin/python3
print("".join([chr(i - (i % 2) * 32) for i in range(122, 96, -1)]), end="")
