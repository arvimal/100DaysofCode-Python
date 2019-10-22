#!/usr/bin/env python3.6

# String substitutions

### 1. The old way of substituion, % substitution.
print("Method 1 : Classic method of string substitution.")
# Example 1:
print("Hello there, I love %s" % ("python"))
# This prints "Hello there, I love python"

# Example 2:
author = "Homer"
book = "Illiad"
print("%s wrote %s\n" % (author, book))
# This prints "Homer wrote Illiad"

### 2. The second method of substitution, `.format()` method.
# Example 1:
print("Method 2 : New method of string substitution.")
print("Hello there, I love {0}".format("python"))

# Example 2:
author = "Homer"
book = "Illiad"
print("{0} wrote {1}\n".format(author, book))


### 3. The latest method of substitution, `f strings`, in Python 3.6 onwards.
print("Method 3 : `f` string method from Python 3.6 onwards.")
# Example 1:
x = "Python"
print(f"Hello there, I love {x}")

# Example 2:
author = "Homer"
book = "Illiad"
print(f"{author} wrote {book}")

# NOTE: The above `f` string format only work in Python 3.6 onwards.
