class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        k=[]
        matrix.reverse()
        for i in range(len(matrix[0])):
            l=[]
            for j in range(len(matrix)):
                l.append(matrix[j][i])
            k.append(l)
        for i in range(len(matrix)):
            matrix[i]=k[i]
        return matrix
