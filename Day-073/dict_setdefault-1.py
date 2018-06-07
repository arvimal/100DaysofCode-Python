#!/usr/bin/env python3

"""
The setdefault() method of a Python dict will set a key and value
if the key does not exist in the dict.

This method can be used to test the existence of a key in the dict,
and insert the key:value if the key does not exist, in a single line.

* Usual method:

```python
if "key" not in my_dict:
    my_dict["key"] = "value"
```

* Using the setdefault() method

This check whether "key" exists in `my_dict`, and if not, insert "key":"value".

```python
my_dict.setdefault("key", "value")
```
"""
import pprint

my_text = "Hello, how are you today?"

count = {}

for char in my_text:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)
