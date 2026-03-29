class Solution:
    def isValid(self, s: str) -> bool:
        valpar = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for par in s:
            if par in valpar:
                if not stack or stack[-1] != valpar[par]: return False
                stack.pop()
            else:
                stack.append(par)
            print(stack)
        
        return not stack