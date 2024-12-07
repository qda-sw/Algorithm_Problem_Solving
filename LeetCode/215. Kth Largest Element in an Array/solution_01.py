# Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Date: 2024.12.07
# Comment: 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]