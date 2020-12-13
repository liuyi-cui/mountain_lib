class Solution(object):

    def chengji(self, x, y):
        return x * y
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from functools import reduce
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        max_num = reduce(self.chengji, nums)
        if max_num < 0:
            return self.maxProduct(nums[:-1])
        return max_num
solu = Solution()
rating = [-4,3,-2]
res = solu.maxProduct(rating)
print(res)