def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    max_string = len(strs[0])
    for string in strs:
        temp = len(string)
        if max_string > temp:
            max_string = temp

    com_prefix = ''
    thing = ''

    curr_max = 0
    curr = 0
    ok = True
    for i in range(0, max_string):
        if ok == False:
            break
            
        ok = True
        thing = thing + strs[0][i]

        for a in range(0, len(strs)):
            if a < len(strs)-1:
                if strs[a][i] != strs[a+1][i]:
                    ok = False
                    thing = ''
                    curr = 0
                    break

        if ok == True:
            curr = curr + 1

            if curr_max < curr:
                curr_max = curr
                com_prefix = thing

    return com_prefix

string = ["flower","flow","flight"]
result = longestCommonPrefix(string)
print(result)