from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = 0
        for i in range(len(nums)):

            diff = max(abs(nums[i]-nums[i-1]), diff)

        return diff






nums = [1,2,5,8,7,10]
obj = Solution()
print(obj.maxAdjacentDistance(nums))