# Test Case 1: The example case from the problem.
nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Expected Output: k=5, nums1 = [0, 1, 2, 3, 4, _, _, _, _, _]

nums2 = []
# Expected Output: k=0, nums2 = []

nums3 = [5]
# Expected Output: k=1, nums3 = [5]

nums4 = [7, 7, 7, 7, 7]
# Expected Output: k=1, nums4 = [7, _, _, _, _]

nums5 = [1, 2, 3, 4, 5]
# Expected Output: k=5, nums5 = [1, 2, 3, 4, 5]

nums6 = [10, 10, 20, 30, 30, 30, 40]
# Expected Output: k=4, nums6 = [10, 20, 30, 40, _, _, _]

nums7 = [1, 1, 2, 3, 4, 5]
# Expected Output: k=5, nums7 = [1, 2, 3, 4, 5, _]

nums8 = [1, 2, 3, 4, 5, 5]
# Expected Output: k=5, nums8 = [1, 2, 3, 4, 5, _]

nums9 = [-5, -5, -4, -3, -3, 0, 1]
# Expected Output: k=5, nums9 = [-5, -4, -3, 0, 1, _, _]

nums10 = [8, 8]
# Expected Output: k=1, nums10 = [8, _]


def remove_duplicates(nums):
    k = 0
    if len(nums) > 1:
        duplicates =[]
        for x in nums:
            if nums.count(x) > 1:
                k+=1
                duplicates.append(x)

        for duplicate in duplicates:
            places = [i for i,v in enumerate(nums) if v == duplicate]
            for x in places[1:]:
                nums.pop(x)
                nums.append(0)

    return k,nums

print(remove_duplicates(nums1))
