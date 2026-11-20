class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        current = 0
        for x in nums:
            if x == 0:
                longest = max(longest, current)
                current = 0
            else:
                current += 1
        return max(longest, current)
