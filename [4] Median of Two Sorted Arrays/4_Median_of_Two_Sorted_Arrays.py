def findMedianSortedArrays(nums1, nums2):
    merge = nums1 + nums2
    merge.sort()
    print(merge)

    length = len(merge)
    if length <= 1:
        return merge[0]
    elif length % 2 == 0:
        median = (merge[int(length/2)-1] + merge[int(length/2)])/2
    else:
        median = merge[int(length/2)]

    return median

list1 = [1, 2]
list2 = [3, 4]

print(findMedianSortedArrays(list1, list2))