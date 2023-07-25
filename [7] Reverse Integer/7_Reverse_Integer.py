def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    negative = False
    if(x < 0):
        negative = True
        x = x - (x * 2)
    
    string = str(x)
    reversed_string = string[::-1]
    # print(reversed_string)
    
    # if reversed_string[0] == '0':
    #     return 0
    
    result = int(reversed_string)
    if result > 2147483647:
        return 0
    elif negative is True:
        return result - (result * 2)
    else:
        return result

    
answer = reverse(1534236469)
print(answer)
    