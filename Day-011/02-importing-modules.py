#!/usr/bin/env python3

# Python comes in with lot of features that are builtin.
# Other features are included in modules, which has to be
# imported to access.
# The default python installation has lots of modules which are
# called the Standard library.

# A module is a single importable file, after which the functions and
# classes can be accessed in the code.

# A module is imported using the `import` keyword/builtin.

import this

print("")
import math
print(math.sqrt(4))

# Import just a specific function, or more
from os import abort, access
from math import pi, sin

# Importing everything
# This is not a good practice and can clutter the namespace,
# as well as cause problems with any functions of the same name.
from sys import *
