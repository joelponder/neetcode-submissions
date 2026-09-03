class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [None] * length * 2
        for i in range(length):
            value = nums[i]
            ans[i] = value
            ans[i+length] =  value
        return nums + nums

