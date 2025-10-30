# third_maximum_number.py
"""
Problem: Third Maximum Number (LeetCode #414)
---------------------------------------------

Given an integer array `nums`, return the **third distinct maximum** number 
in this array. If the third maximum does not exist, return the maximum number.

Examples:
----------
Input: nums = [3,2,1]
Output: 1

Input: nums = [1,2]
Output: 2

Input: nums = [2,2,3,1]
Output: 1

Constraints:
------------
- 1 <= len(nums) <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Follow-up:
-----------
Can you find an O(n) solution?
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')

        for num in nums:
            if num in (first, second, third):
                continue
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        
        return third if third != float('-inf') else first