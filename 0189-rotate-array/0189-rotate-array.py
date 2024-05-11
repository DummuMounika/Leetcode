class Solution(object):
    def rotate(self, nums, k):
        l= len(nums)
        if k>l:
            k=k%l
        #for reversing whole array
        i=0
        j=l-1
        while i <= j:
            temp1= nums[i]
            temp2= nums[j]
            nums[i] = temp2
            nums[j] = temp1
            i += 1
            j -= 1
        #for reversing first k elements
        i=0
        j=k-1
        while i <= j:
            temp1= nums[i]
            temp2 = nums[j]
            nums[i] = temp2
            nums[j] = temp1
            i += 1
            j -= 1
        #for reversing remaining k elements
        i=k
        j=l-1
        while i <= j:
            temp1= nums[i]
            temp2 = nums[j]
            nums[i] = temp2
            nums[j] = temp1
            i += 1
            j -= 1
        return nums

        