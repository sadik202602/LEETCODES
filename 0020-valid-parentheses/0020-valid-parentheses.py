class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        parentheses_pair = {")" : "(",
                            "}" : "{",
                            "]" : "["
                            }
        
        for cat in s:
            if cat in "({[":
                stack.append(cat)
            else:
                if not stack:
                    return False
                    
                elif stack[-1] == parentheses_pair[cat]:
                    stack.pop()
                        
                else:
                    return False
                    
        return not stack
        