def lengthOfLongestSubstring(s):
    max_length = 0
    start = 0
    dictionary = {}

    for end in range(len(s)):
        if s[end] in dictionary:
            start = max(start, dictionary[s[end]] + 1)

        dictionary[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

result = lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
print(result)