class Solution(object):
    def majorityElement(self, nums):
        k = len(nums)//2
        dictElement= {}
        for num in nums:#time complexity O(7)
            if not dictElement.__contains__(num):
                dictElement.__setitem__(num,1)
            else:
                count = dictElement.get(num)+1
                dictElement.__setitem__(num,count)
            if dictElement[num] > k:
                return num
        