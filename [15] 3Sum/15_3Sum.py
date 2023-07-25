def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    list = []
    nums.sort()
    # print(nums)

    for i in range(0, len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i + 1
        right = len(nums)-1
        
        while(left < right):
            sum = nums[i] + nums[left] + nums[right]
            # print(sum, nums[i], nums[left], nums[right])
            if(sum == 0):
                list.append((nums[i], nums[left], nums[right]))
                left = left + 1
                right = right - 1

                while left < right and nums[left] == nums[left-1]:
                    left = left + 1
                while left < right and nums[right] == nums[right+1]:
                    right = right - 1
            elif sum < 0:
                left = left + 1
            else:
                right = right - 1
    
    return list

result = threeSum([-1,0,1,2,-1,-4])
print(result)