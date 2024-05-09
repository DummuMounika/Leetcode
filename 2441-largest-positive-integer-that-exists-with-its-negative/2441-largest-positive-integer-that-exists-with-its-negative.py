class Solution(object):
    def findMaxK(self, nums):
        max=-1
        setN= set(nums)
        for num in nums:
            x= num * -1 
            if x in setN:
                temp = x
                if temp > max:
                    max= temp                
        return max