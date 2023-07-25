def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    left = 0
    right = len(height)-1
    curr_area = 0

    while (left < right):
        area = min(height[left], height[right]) * (right-left)
        curr_area = max(curr_area, area)

        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1

    return curr_area

result = maxArea([1,8,6,2,5,4,8,3,7])
print(result)