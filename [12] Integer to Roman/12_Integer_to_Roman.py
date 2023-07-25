def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """

    dictionary = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    string = ""

    for key, value in dictionary.items():
        while num > 0 and num >= key:
            num = num - key
            string = string + value

    return string

result = intToRoman(58)
print(result)