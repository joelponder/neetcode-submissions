class Solution:
    def __init__(self):
        self.memoized = {}
    def climbStairs(self, n: int) -> int:
        if n in self.memoized:
            return self.memoized[n]
        elif n < 3:
            return n
        else: 
            result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.memoized[n] = result
            return result
        