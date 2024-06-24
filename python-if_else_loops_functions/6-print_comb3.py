#!/usr/bin/python3
print(", ".join([f"{i:02d}" for i in range(100) if i // 10 < i % 10]))
