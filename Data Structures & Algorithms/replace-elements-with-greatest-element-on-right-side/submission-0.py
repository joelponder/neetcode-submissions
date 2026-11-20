class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        biggest = arr[i]
        arr[i] = -1
        i -= 1
        while i > -1:
            this = arr[i]
            arr[i] = biggest
            biggest = max(biggest, this)
            i -= 1
        return arr
 
        