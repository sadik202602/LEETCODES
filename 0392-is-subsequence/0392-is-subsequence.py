class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        
        i = 0
        k = 0
        mt = []
        
        for kot in t:
            if i < len(s) and s[i] == t[k]:
                mt.append(t[k])
                i += 1
            k += 1
           
        if len(s) == len(mt):
            return True
        else: 
            return False
              
        