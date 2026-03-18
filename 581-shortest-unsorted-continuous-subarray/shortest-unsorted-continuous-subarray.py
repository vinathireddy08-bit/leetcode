class Solution(object):
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        n = len(nums)

        left = 0
        while left < n and nums[left] == sorted_nums[left]:
            left += 1

        right = n - 1
        while right >= 0 and nums[right] == sorted_nums[right]:
            right -= 1

        if right <= left:
            return 0

        return right - left + 1