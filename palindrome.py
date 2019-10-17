"""This module named palindrome"""
from collections import deque

"""This function named as is_palindrome, validate if input is palindrome"""
def is_palindrome(p):

    md1 = deque(p)
    md2 = []
    md2 = deque(maxlen=len(md1))

    for x in deque(md1):
        md2.appendleft(x)


    if type(p) is not str:
        raise ValueError
    if not p:
        return False
    if deque(md1) == deque(md2):
        return True
    else:
        return False
