def maxProductDifference(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxDiff = 0

    nums.sort()
    maxDiff = nums[0] * nums[1] - nums[len(nums)-1] * nums[len(nums)-2]
    print(-maxDiff)


answer = maxProductDifference(nums=[5, 6, 2, 7, 4])
print(answer)
