# What id Valid Parenthesis?
#   Every Bracket must be closed by same type
#   Every Bracket must have their closing

# Using Stack
# 1) brackets is not of same type [False]
# 2) At the end, stack is not empty [False]
# 3) If you find closing, but stack is empty [False]


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(":")", "[":"]", "{":"}"}
        stack = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) > 0:
                    x = stack.pop()
                else:
                    return False
                if dic[x] != i:
                    return False

        if len(stack) == 0:
            return True
        return False