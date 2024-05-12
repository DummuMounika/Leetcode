class Solution(object):
    def groupAnagrams(self, strs):
        # Check for empty strings
        if len(strs) <= 1 or strs is None:
            return [strs]  
        res = []
        dictA = {}
        for word in strs:
            # Count frequency of characters in the word
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1   
            # Convert frequency list to a tuple for dictionary key
            key = tuple(freq)
            
            if key not in dictA:
                dictA[key] = len(res)
                res.append([word])
            else:
                res[dictA[key]].append(word)
        return res
    
    

       
        