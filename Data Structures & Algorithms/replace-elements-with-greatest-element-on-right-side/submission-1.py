class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = -1
        for i in range(len(arr)-1, -1, -1):
            this = arr[i]
            arr[i] = biggest
            biggest = max(biggest, this)
        return arr
 
        