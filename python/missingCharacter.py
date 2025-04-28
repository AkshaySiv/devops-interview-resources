"""
Question:
Write a Python function `missingCharacters` that takes a string `s` as input and returns a string containing the missing digits (0-9) 
and lowercase English letters (a-z) that are not present in `s`. 
The returned string should have the missing characters in sorted order.
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import string




#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    digit={"0","1","2","3","4","5","6","7","8","9"}
    letter=set(string.ascii_lowercase)
    digitPresentList=set()
    lettersPresentList=set()
    for i in range(0, len(s)-1):
        if s[i] in digit:
            digitPresentList.add(s[i])
        else:
            lettersPresentList.add(s[i])

    diffletter = letter - lettersPresentList
    diff = digit - digitPresentList
    print (diff)
    print (diffletter)
    result = sorted (diff | diffletter)
    myString = "".join(result)
    print (myString)

if __name__ == '__main__':

    # s = input()

    result = missingCharacters("8hypotheticall024y6wxz")

    # fptr.write(result + '\n')

    # fptr.close()
