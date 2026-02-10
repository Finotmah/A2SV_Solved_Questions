from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        nums = sorted(count, key = lambda x: count[x], reverse = True)
        
        top_ks = []
        for i in range(k):
            top_ks.append(nums[i])
            
        return top_ks
