class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        if len(nums2) == 0:
            return None
        
        dictM = {}
        result = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            #if stack is not empty, then compare it's last element with nums2[i]
            while stack and nums2[i] > stack[-1]:
                dictM[stack[-1]] = nums2[i]
                stack.pop()  #since we found a pair for the top element, remove it.
            stack.append(nums2[i])
        
        for element in stack:
            dictM[element] = -1 

        print(dictM)

        for i in range(len(nums1)):
            result.append(dictM[nums1[i]])

        return result 


        