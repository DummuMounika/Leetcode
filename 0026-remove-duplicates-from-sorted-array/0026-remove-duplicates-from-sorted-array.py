class Solution(object):
    def removeDuplicates(self, nums):
        i=1
        k=0
        while i < len(nums):
            if nums[i] == nums[k]:
                i+=1
                continue
            else:
                k+=1
                nums[k]=nums[i]
        return k+1
        
            