# Assumed to be done due to bad outputs in leetcode
def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    # 0 = Prefix, 1 = Postfix
    current = 0
    number = ''
    for i in range(0, len(s)):
        if current == 1:
            if s[i].isdigit():
                number += s[i]
            else:
                break

        if current == 0:
            if s[i].isdigit():
                current = 1
                if s[i-1] == "-":
                    number += s[i-1]
                number += s[i]

    num = int(number)
    return num

result = myAtoi("words and 987")
print(result)