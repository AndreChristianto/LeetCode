def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    result = s[0]
    length_max = 1
    for i in range(0, len(s)):
        length = 1
        # Check for odd
        # print("odd")
        curr = i
        curr1 = curr-1
        curr2 = curr+1
        while curr1 >= 0 and curr2 < len(s):
            # print("current1:", curr1)
            # print("current2:", curr2)
            if s[curr1] == s[curr2]:
                length += 2
                if length_max < length:
                    # print("yes")
                    # print("current1:", curr1)
                    # print("current2:", curr2)
                    result = s[curr1:curr2+1]
                    # print(length_max)
                    # print(length)
                    # print(result)
                    length_max = length
                    # print("length max: ", length_max)
                curr1 -= 1
                curr2 += 1
            else:
                break

        # Check for even
        # print("even")
        length = 0
        curr = i
        curr1 = curr
        curr2 = curr+1
        if curr1 >= 0 and curr2 < len(s) and s[curr1] == s[curr2]:
            while curr1 >= 0 and curr2 < len(s):
                # print("current1:", curr1)
                # print("current2:", curr2)
                if s[curr1] == s[curr2]:
                    length += 2
                    if length_max < length:
                        # print("yes")
                        # print("current1:", curr1)
                        # print("current2:", curr2)
                        result = s[curr1:curr2+1]
                        # print(length_max)
                        # print(length)
                        # print(result)
                        length_max = length
                        # print(length_max)
                    curr1 -= 1
                    curr2 += 1
                else:
                    break

    return result
    
result = longestPalindrome("babad")
print(result)