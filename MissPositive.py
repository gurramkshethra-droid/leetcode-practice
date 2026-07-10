class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        s=1
        while s in nums:
                s+=1
        return s
