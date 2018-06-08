#!/usr/bin/env python3

# Flow control in loops can be decided using
# `break` and `continue`.

# 1. break
# break is used to break out of a loop if a
# specific condition hits.
# In this case, if i ever hits 5, the loop terminates printing
print("Example 1 : break")
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 2. continue
# `continue` skips an iteration or continue with the next.
print("Example 2 : continue")
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue
    print(i)
    if i == 5:
        break
    i += 1
