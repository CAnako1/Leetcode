"""
Valid Parethesis

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

## Solution
"""
Use a stack data structure as we will match closing brackets to opening ones and remove from stack as they match
Use a hash map to match the correct opening brackets to a closing one
Look through brackets in s and check if it is a closing bracket - if yes, make sure stack is not empty
If they match (the closing and opening), then pop them from the stack
if they dont match return False 
If item being looped through is an open bracket, then append it to the stack
Return True if our stack is empty (if not stack)that means we found a closing item for each open item, 
else return False 


"""

class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False