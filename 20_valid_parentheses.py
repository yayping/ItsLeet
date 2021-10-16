"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket = {"(": ")", "[": "]", "{": "}"}
        open_bracket = set(["(", "[", "{"])
        stack = []
        
        for i in s:
            if i in open_bracket:
                stack.append(i)
            elif stack and i == bracket[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []