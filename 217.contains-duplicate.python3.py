#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (46.69%)
# Total Accepted:    194.6K
# Total Submissions: 416.7K
# Testcase Example:  '[]'
#
# 
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
# 
#
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
