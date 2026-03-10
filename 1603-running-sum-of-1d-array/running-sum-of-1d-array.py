class Solution(object):
    def runningSum(self, nums):
        count = 0
        new = []
        for i in range(len(nums)):
            count = count + nums[i]
            new.append(count)
        return new 
        