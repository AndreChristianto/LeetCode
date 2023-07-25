def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    curr = 3000
    nums.sort()
    for i in range(0, len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i+1
        right = len(nums)-1

        while(left < right):
            sum = nums[i] + nums[left] + nums[right]

            if(abs(target - curr) > abs(target - sum)):
                print("left: ", nums[left])
                print("right: ", nums[right])
                print("sum: ", curr)
                print("")
                curr = sum

                left = left + 1
                right = right - 1

                while nums[left] == nums[left - 1]:
                    left = left + 1
                while nums[right] == nums[right + 1]:
                    right = right + 1
            elif sum < target:
                left = left + 1
            else:
                right = right - 1

    return curr

    # for i in range(0, len(nums)-2):
    #     for j in range(i+1, len(nums)-1):
    #         for k in range(j+1, len(nums)):
    #             sum = nums[i] + nums[j] + nums[k]
    #             print(sum)
    #             thing = target - sum
                
    #             print("curr: ", curr)
    #             print("thing: ", thing)
    #             if abs(target - curr) > abs(thing):
    #                 curr = sum

    # return curr

result = threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
print("result: ", result)