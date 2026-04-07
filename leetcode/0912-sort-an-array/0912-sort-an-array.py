class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            i = 0
            j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])

            return res

        def mergesort(num):
            if len(num) <= 1:
                return num
            mid = len(num)//2

            left = mergesort(num[:mid])
            right = mergesort(num[mid:])

            return merge(left,right)
        return mergesort(nums)