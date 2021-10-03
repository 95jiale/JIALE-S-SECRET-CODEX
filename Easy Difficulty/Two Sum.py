class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for x in range(len(nums)):
            # loops the entire array as x > 2,7,11,15
            for y in range(x+1, len(nums)):
                # loops (x+1 , entire array after x+1) > (2,7)>(2,11,)... > (7,11)>(7,15)...> (11,15) > end
                if nums[x] + nums[y] == target:
                    return [x, y]
