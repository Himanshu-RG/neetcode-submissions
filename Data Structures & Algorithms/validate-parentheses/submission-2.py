class Solution:
    def isValid(self, s: str) -> bool:
        param = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for i in s:
            if i in param:
                if stack and stack[-1] == param[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)  
        
        return True if not stack else False