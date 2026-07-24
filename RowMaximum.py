class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        l=[]
        c=0
        maxm=0
        for idx,i in enumerate(mat):
            count=0
            for j in i:
                if j==1:
                    count+=1
            if maxm<count:
                maxm=count
                c=idx
        l.append(c)
        l.append(maxm)
        return l
