#!/usr/bin/python3
print("{}".format("".join([chr(i) if i % 2 == 0 else chr(i).upper()
      for i in range(122, 96, -1)])), end="")
