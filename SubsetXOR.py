class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sum=0
        for i in range(1<<n):
            x=0
            for j in range(n):
                if ((1<<j)&i):
                    x^=nums[j]
            sum+=x
        return sum
