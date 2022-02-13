def countKDifference(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    count = 0
    for x in range(len(nums)):
        for y in range(x+1, len(nums), 1):
            if abs(nums[x]-nums[y]) == k:
                count = count + 1
    print(count)


answer = countKDifference(nums=[3, 2, 1, 5, 4], k=2)
print(answer)
