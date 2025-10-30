# remove_duplicates_sorted_array.py
"""
Problem: Remove Duplicates from Sorted Array
--------------------------------------------

Given an integer array `nums` sorted in non-decreasing order, 
remove the duplicates **in-place** such that each unique element appears only once. 
The relative order of the elements should be kept the same.

After removing the duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in sorted order. 
The remaining elements beyond index `k - 1` can be ignored.

---

Example 1:
----------
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation:
Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.

Example 2:
----------
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation:
Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.

---

Constraints:
------------
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.

---

Approach:
----------
We use the **Two-Pointer Technique** to solve this in O(n) time and O(1) space.

1. Initialize `unique_index = 0` to track the position of the last unique number.
2. Traverse the array with another pointer `i` starting from index 1.
3. Whenever we find a new unique number (`nums[i] != nums[unique_index]`),
   increment `unique_index` and copy `nums[i]` to `nums[unique_index]`.
4. Finally, return `unique_index + 1` — the count of unique numbers.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]

        return unique_index + 1

