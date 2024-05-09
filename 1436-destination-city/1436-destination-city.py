class Solution(object):
    def destCity(self, paths):
        setcity = set()
        for path in paths:
            setcity.add(path[0])
        #print(setcity)
        for path in paths:
            dest = path[1]
            if dest not in setcity:
                return dest
        return ""


        
        

