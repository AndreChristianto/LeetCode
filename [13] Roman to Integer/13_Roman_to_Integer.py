def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    total = 0
    curr = 0
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

    while(curr < len(s)):
        if curr + 1 != len(s) and s[curr:curr + 2] in roman:
            total += roman[s[curr:curr + 2]]
            curr += 2
        else:
            total += roman[s[curr]]
            curr += 1
    return total

result = romanToInt('VIII')
print(result)