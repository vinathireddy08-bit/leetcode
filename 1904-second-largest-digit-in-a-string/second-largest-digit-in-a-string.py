class Solution(object):
    def secondHighest(self, s):
        new = []
        for ch in s:
            if ch.isdigit():
                new.append(int(ch))
        
        unique_nums = sorted(set(new),reverse = True)

        if len(unique_nums)<2:
            return -1


        return unique_nums[1]