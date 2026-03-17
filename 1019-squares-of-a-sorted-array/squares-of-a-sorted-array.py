class Solution(object):
    def sortedSquares(self, nums):
        squares = [x*x for x in nums]
        squares.sort()
        return squares 
        