# Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Date: 2024.12.07
# Comment: Time Complexity를 비교해보기 위하여 List를 사용한 PriorityQueue도 구현함. -> Fail

class PriorityQueue:
    def push(self, num):
        raise Exception("Not implemented")
    def pop(self):
        raise Exception("Not implemented")
    def top(self):
        raise Exception("Not implemented")
class Heap(PriorityQueue):
    def __init__(self):
        self.heap = []
    def _parent(self, i)->int:
        return (i - 1) // 2
    def _left(self, i)->int:
        return 2 * i + 1
    def _right(self, i)->int:
        return 2 * i + 2
    def _can_access(self, i)->bool:
        return 0 <= i < len(self.heap)
    def _downheap(self, i)->None:
        smallest = i
        left = self._left(i)
        right = self._right(i)
        if self._can_access(left) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if self._can_access(right) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._downheap(smallest)
    def _upheap(self, i)->None:
        if self._can_access(self._parent(i)) and self.heap[self._parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            self._upheap(self._parent(i))
    def heappush(self, num):
        self.heap.append(num)
        self._upheap(len(self.heap) - 1)
    def heappop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._downheap(0)
        return result
    def _top(self):
        return self.heap[0]

    def push(self, num):
        self.heappush(num)
    def pop(self):
        return self.heappop()
    def top(self):
        return self._top()
class ListPriorityQueue(PriorityQueue):
    def __init__(self):
        self.heap = []
    def push(self, num):
        self.heap.append(num)
        self.heap.sort()
    def pop(self):
        return self.heap.pop(0)
    def top(self):
        return self.heap[0]
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = ListPriorityQueue()
        for e in nums:
            heap.push(-e)
        klarge = []
        for i in range(k):
            klarge.append(-heap.pop())
        return klarge[k-1]

nums = [3,2,1,5,6,4]
print(Solution().findKthLargest(nums, 2))