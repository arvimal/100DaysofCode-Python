#!/usr/bin/env python3

"""
Introspection is the process of understanding oneself.
Here, we use Python's builtins to understand about Python.
This can be helpful in case the module comes with not-so-good
documentation.

The most useful builtins to understand about an object

type
dir
help

* type
`type` helps to understand what sort of class has the instance
been instantiated from.

* dir
`dir()` helps to list the methods available for that instance.
This actually lists the methods from the class which the instance
was instantiated from.
It is also useful to list the names in the current namespace, if
no args are passed to dir().

* help()
`help(<module-name>)` prints the document strings of a builtin or module.
Without arguments, it presents a `help>` prompt which can be used to
navigate the help system in built.
"""


a = "test"
print(type(a))

import sys

dir(sys)

help(sys)
