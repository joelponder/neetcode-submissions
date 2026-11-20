class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, c  = 0, 0
        while c < len(nums):
            if nums[c] != val:
                if c != l:
                    nums[l] = nums[c]
                l += 1
            c += 1
        return l
