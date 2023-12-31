def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x /= 10

    if x == rev or x == rev / 10:
        return True
    
result = isPalindrome(121)
print(result)