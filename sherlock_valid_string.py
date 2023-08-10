#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    def isValid(s):
    # Dictionary where keys are unique letters of the string and values
    # are associated frequencies of those letters in the string.
    string = [*s]
    dict = {}
    for letter in string:
        if letter in dict.keys():
            dict[letter] += 1
        else:
            dict[letter] = 1
    # Split strings into three cases, use set to compare unique letter frequencies.
    vals = dict.values()
    sorted_vals = sorted(vals)
    # Case 1: All letters in the string occur the same number of times. 'aaabbbccc'
    if len(set(sorted_vals)) == 1:
        return 'YES'
    # Case 2: All but one letter in the string occur the same number of times and outlier
    # occurs only one time. 'abbbcccdddeee'
    elif sorted_vals[0] ==1 and len(set(sorted_vals[1:])) == 1:
        return 'YES'
    # Case 3: There are two frequencies and they have an absolute difference of one.
    # 'aaaafffff'
    else:
        bigger_val = sorted_vals[-1]
        sorted_vals[-1] = bigger_val - 1
        if len(set(sorted_vals)) == 1:
            return 'YES'
        else:
            return 'NO'




if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
