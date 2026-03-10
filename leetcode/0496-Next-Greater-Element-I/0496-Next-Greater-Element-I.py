class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = [-1]*len(nums1)
        stack = []
        mymap = {}

        for num in nums2:
            while stack and stack[-1] < num:
                mymap[stack.pop()] = num
            stack.append(num)
            
        for i, num in enumerate(nums1):
            if num in mymap:
                res[i] = mymap[num]
        return res