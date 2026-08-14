class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sid = {}
        kid = {}
        
        for sef in s:
            if sef in sid:
                sid[sef] += 1
            else:
                sid[sef] = 1
                
                
        for nef in t:
            if nef in kid:
                kid[nef] +=1
            else:
                kid[nef] = 1
        
        
        if sid == kid:
            return True
        else:
            return False
            