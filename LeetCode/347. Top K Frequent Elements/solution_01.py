# Problem: https://leetcode.com/problems/top-k-frequent-elements/description/
# Date: 2024.12.07
# Comment: 실전 풀이
from collections import *
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [x[0] for x in heapq.nlargest(k, count.items(), key=lambda x:x[1])]