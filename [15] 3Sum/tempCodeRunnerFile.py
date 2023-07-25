    sum = nums[i] + nums[left] + nums[right]
            print(sum, nums[i], nums[left], nums[right])
            if(sum == 0):
                thing = []
                thing.append(nums[i])
                thing.append(nums[left])
                thing.append(nums[right])
                list.append(thing)
            else:
                if sum < 0:
                    left = left + 1
                else:
                    right = right - 1