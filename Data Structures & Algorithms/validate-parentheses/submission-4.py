class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            if i == ')':
                if len(stack) == 0:
                    return False
                if stack.pop() != '(':
                    return False
            if i == '{':
                stack.append(i)
            if i == '}':
                if len(stack) == 0:
                    return False
                if stack.pop() != '{':
                    return False
            if i == '[':
                stack.append(i)
            if i == ']':
                if len(stack) == 0:
                    return False
                if stack.pop() != '[':
                    return False
        return not stack