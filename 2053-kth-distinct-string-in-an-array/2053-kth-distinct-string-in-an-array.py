class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dictk = dict()
        for i in range(len(arr)):
            if arr[i] not in dictk:
                dictk[arr[i]] = 1
            else:
                val = 1
                dictk[arr[i]] += val
        for i in range(len(arr)):
            if dictk[arr[i]] == 1:
                k -= 1
            if(k==0):
                return arr[i]
        return ""
                