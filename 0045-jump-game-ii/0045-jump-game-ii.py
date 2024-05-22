class Solution(object):
    def jump(self, nums):
        goalIndex = 0
        jumpCount = 0
        prevgoalIndex = 0
        if len(nums) <= 1:
            return 0 
        for i in range(len(nums)):
            if i + nums[i] >= goalIndex:
                goalIndex = i + nums[i]
                
            if i == prevgoalIndex:
                jumpCount += 1
                prevgoalIndex = goalIndex
                if prevgoalIndex >= len(nums)-1:
                    return jumpCount
            
        
        