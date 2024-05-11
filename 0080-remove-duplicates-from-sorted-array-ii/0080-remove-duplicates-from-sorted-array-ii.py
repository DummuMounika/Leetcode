class Solution(object):
    def removeDuplicates(self, nums):
        count=1
        i=1
        k=0
        while i < len(nums):
            if nums[i] == nums[k]:
                count+=1
                if count <= 2:
                    k+=1
                    nums[k] = nums[i]
            else:
                k+=1
                nums[k] = nums[i]
                count = 1
            i+=1
        return k+1
        