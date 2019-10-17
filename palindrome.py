
 # Palindrome 

from collections import deque

#  Defining a function named as palindrome
def is_palindrome(inputpal):

    md1 = deque(inputpal)
    md2 = []
    md2 = deque(maxlen=len(md1))

    for x in deque(md1):
        md2.appendleft(x)


    if type(inputpal) is not str:
        raise ValueError
    if not inputpal:
        return False
    if deque(md1) == deque(md2):
        return True
    else:
        return False
