#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (33.87%)
# Total Accepted:    289.4K
# Total Submissions: 854.5K
# Testcase Example:  '"["'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
# 
#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for c in s:
            if c in "([{":
                stk.append(c)
                continue
            elif c == ')':
                if not stk or stk[-1] != '(':
                    return False
            elif c == ']':
                if not stk or stk[-1] != '[':
                    return False
            elif c == '}':
                if not stk or stk[-1] != '{':
                    return False
            stk.pop()
        return not stk
