"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

# Solution

class Solution(object):
    def longestCommonPrefix(self, strs):
        pre = strs[0]
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        return(pre)