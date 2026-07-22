class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxi=-1
        for i in range(len(arr)-1,-1,-1):
            temp=arr[i]
            arr[i]=maxi
            if maxi<temp:
                maxi=temp
        return arr
        
