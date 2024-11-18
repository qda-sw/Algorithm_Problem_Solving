class Solution:
    def pathSum(self, root, targetSum: int):
        def left(n):
            return 2*n+1
        def right(n):
            return 2*n+2
        def is_none(n):
            return n >= len(root) or root[n] == -1
        
        def recurse(cur:int, target:int, temp:list, history:list):
            if is_none(cur):
                return
            temp.append(root[cur])
            if is_none(left(cur)) and is_none(right(cur)) and target == root[cur]:
                history.append(temp)
                return history
            target -= root[cur]
            recurse(left(cur), target, temp[::], history)
            recurse(right(cur), target, temp[::], history)

            return history

        result =  recurse(0, targetSum, [], [])
        if result == None:
            return []
        else:
            return result
        
root_00 = [
    5,                          # root
    4, 8,                       # level 1
    11, -1, 13, 4,              # level 2
    7, 2, -1, -1, -1, -1, 5, 1  # level 3
]
root_01 = [
    1,
    2, 3
]
root_02 = [
    1,
    2
]
sol = Solution()
print(sol.pathSum(root_00, 22) == [[5,4,11,2],[5,8,4,5]])
print(sol.pathSum(root_01, 5) == [])
print(sol.pathSum(root_02, 0) == [])