#!/usr/bin/env python3

# 1. Reading files

# 1.1. Read files line by line
handle = open("/tmp/new.txt", "r")
for line in handle:
    print(line)
handle.close()

# 1.2. Read file in chunks
handle = open("/tmp/new.txt", "r")
data = handle.read(1024)  # Read 1024 / 1KB of data
print(data)
handle.close()

# 1.3. Read binary files
handle = open("/tmp/new.img", "rb")
