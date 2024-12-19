"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.
"""

#Solution

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        isPalindrome = True if x[::-1] == x else False
        return isPalindrome