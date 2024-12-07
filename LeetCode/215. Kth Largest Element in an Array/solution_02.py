# Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Date: 2024.12.07
# Comment: heapq 모듈의 nlargest 함수를 사용.

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[k-1]