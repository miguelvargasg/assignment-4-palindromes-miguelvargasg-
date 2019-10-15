from palindrome import is_palindrome

def test_is_palindrome_1():
    assert is_palindrome('') == False

def test_is_palindrome_2():
    assert is_palindrome('a') == True

def test_is_palindrome_3():
    assert is_palindrome('bb') == True

def test_is_palindrome_4():
    assert is_palindrome('abc') == False

def test_is_palindrome_5():
    assert is_palindrome('laval') == True

def test_is_palindrome_6():
    assert is_palindrome('toronto') == False

def test_is_palindrome_7():
    assert is_palindrome('Able was I ere I saw elbA') == True
