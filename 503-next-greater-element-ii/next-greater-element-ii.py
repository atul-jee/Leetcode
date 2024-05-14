from collections import defaultdict

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        d = defaultdict(int)
        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                d[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)

        for i in range(n):
            result[i] = d.get(i, -1)

        return result
