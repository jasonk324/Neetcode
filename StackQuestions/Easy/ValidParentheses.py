class Solution(object):
    def isValid(self, s):
        stack = []
        matchingDict = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char not in matchingDict:
                stack.append(char)
                continue
            else:
                if len(stack) == 0 or matchingDict[char] != stack[-1]:
                    return False
            stack.pop()

        if len(stack) == 0:
            return True
        else: 
            return False