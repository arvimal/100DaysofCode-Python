#!/usr/bin/env python3

"""
https://leetcode.com/problems/defanging-an-ip-address/

1108. Defanging an IP Address - Easy

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Constraints: The given address is a valid IPv4 address.
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        print(address.replace(".", "[.]"))
        return address.replace(".", "[.]")

Test = Solution()
Test.defangIPaddr("1.2.3.4")
Test.defangIPaddr("192.168.10.100")
Test.defangIPaddr("192.168.109.10")
Test.defangIPaddr("10.15.210.4")
