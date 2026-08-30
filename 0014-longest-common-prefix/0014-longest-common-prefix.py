class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''
        
        first_word = strs[0]
        
        
        for i in range(len(first_word)):
            first_character = first_word[i]
            
            for other_word in strs:
                if i == len(other_word) or other_word[i] != first_character:
                    return first_word[:i]
                
        return first_word       
        

        