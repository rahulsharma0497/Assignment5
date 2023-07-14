def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    distinct_nums1 = [num for num in nums1 if num not in set2]
    distinct_nums2 = [num for num in nums2 if num not in set1]

    return [distinct_nums1, distinct_nums2]
