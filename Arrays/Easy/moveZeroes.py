# move_zeroes.py
"""
Problem: Move Zeroes
--------------------
Given an integer array `nums`, move all zeros to the end while maintaining
the relative order of non-zero elements. The operation must be done in-place.

Example:
--------
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Constraints:
------------
- 1 <= len(nums) <= 10^4
- nums[i] is an integer.

Approach:
---------
Use two-pointer technique:
1. Move all non-zero elements to the beginning.
2. Fill the remaining indices with zeros.
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        
        return nums