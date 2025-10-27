#!/bin/bash
#
# Solution of the easy problem
# https://leetcode.com/problems/valid-phone-numbers/
# "Valid Phone Numbers"
#
grep -e "^[0-9]\{3\}\-[0-9]\{3\}\-[0-9]\{4\}$" -e "^([0-9]\{3\}) [0-9]\{3\}\-[0-9]\{4\}$" file.txt

