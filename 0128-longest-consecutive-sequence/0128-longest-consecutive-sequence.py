class Solution(object):
    def longestConsecutive(self, nums):
        numsset= set(nums)
        maxL=0
        l=0
        for num in nums:
            if not numsset.__contains__(num-1):
                end= num
                l=1
                while numsset.__contains__(end+1):
                    end += 1
                    l += 1
                    if l > maxL:
                        maxL = l
        if l > maxL:
            maxL = l
        return maxL