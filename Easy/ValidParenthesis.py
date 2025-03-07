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



"""
Brute Force approach
Look at the string and check for the pairs, replace them with empty strings
return the string
"""

def isValid(s: str) -> bool:
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')
    return s == ''


"""
Alternative approach to the one on top - with notes for clarity
"""

def isValid(s: str) -> bool:
    stack = []
    closed = {']': '[', ')': '(', '}': '{'}

    for i in s:
        if i not in closed:  # If it's an opening bracket, push it onto the stack
            stack.append(i)
        else:  # If it's a closing bracket
            if stack and stack[-1] == closed[i]:  # Match with the last opening bracket
                stack.pop()
            else:  # Mismatch or empty stack
                return False

    return not stack  # If the stack is empty, all brackets are properly matched
