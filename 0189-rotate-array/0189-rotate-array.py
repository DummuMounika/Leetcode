class Solution(object):
    def rotateArray(self,nums,i,j):
        while i <= j:
            temp1= nums[i]
            temp2 = nums[j]
            nums[i] = temp2
            nums[j] = temp1
            i += 1
            j -= 1
        return nums

    def rotate(self, nums, k):
        l= len(nums)
        if k>l:
            k=k%l
        #for reversing whole array
        nums = self.rotateArray(nums, 0,l-1) 
        #for reversing first k elements
        nums = self.rotateArray(nums, 0,k-1) 
        #for reversing remaining k elements
        nums = self.rotateArray(nums, k,l-1)
        return nums

        