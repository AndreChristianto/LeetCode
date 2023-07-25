def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    result = []
    length = len(s)
    difference = numRows * 2 - 2
    
    for row in range(0, numRows):
        if length <= numRows or numRows == 1:
            return s
        else:
            left_difference = difference - (row * 2)
            right_difference = row * 2

            curr = row
            # print("curr: ", curr)
            # print("scur: ", s[curr])
            # print("curr: ", curr)
            result += s[curr]
            while curr < length:
                curr += left_difference
                if left_difference > 0:
                    # print("curr: ", curr)
                    if curr < length:
                        result += s[curr]

                curr += right_difference
                if right_difference > 0:
                    # print("curr: ", curr)
                    if curr < length:
                        result += s[curr]

            left_difference -= 2
            right_difference += 2

    result = ''.join(result)
    return result


answer = convert("AB", 1)
print(answer)