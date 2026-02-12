from collections import Counter

class Solution(object):
    def minimumIndex(self, nums):

        total_count = Counter(nums)

        # find global dominant element
        dominant_element = 0
        max_frq = 0

        for num in total_count:
            if total_count[num] > max_frq:
                max_frq = total_count[num]
                dominant_element = num

        left_count = 0
        size1 = 0
        size2 = len(nums)

        # try splits
        for i in range(len(nums)-1):

            size1 += 1
            size2 -= 1

            if nums[i] == dominant_element:
                left_count += 1

            right_count = max_frq - left_count

            if left_count > size1//2 and right_count > size2//2:
                return i

        return -1
