# two_sum.py
"""
Problem: Two Sum
Given an array of integers `nums` and an integer `target`, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]

Optimized solution using Hash Map for O(n) time complexity.
"""



# brute-force solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
        
    



# optimized solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            complement = target- num
            if compement in hashMap:
                return [hashMap[complement], i]
            hashMap[num] = i
