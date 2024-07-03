class Solution(object):
    def intersect(self, nums1, nums2):
        repL = []
        dictN = {}
        for num1 in nums1:
            if not num1 in dictN:
                dictN[num1] = 1
            else:
                val = 1
                dictN[num1] += val
        print(dictN)
        for num2 in nums2:
            if num2 in dictN and dictN[num2] > 0:
                repL.append(num2)
                dictN[num2] -= 1
        return repL
            


        
        