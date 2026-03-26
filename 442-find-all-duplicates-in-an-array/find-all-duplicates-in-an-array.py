class Solution(object):
    def findDuplicates(self, nums):
        duplicates = []
        seen = set()

        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)

        return duplicates