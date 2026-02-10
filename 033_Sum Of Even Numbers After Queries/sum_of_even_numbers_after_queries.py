class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sum_even = 0
        answer = []
        for num in nums:
            if num % 2 == 0:
                sum_even += num
        for query in queries:
            
            index = query[1]
            value = query[0]
            pre_value = nums[index]
            if pre_value % 2 == 0:
                sum_even -= pre_value

            nums[index] = nums[index] + value

            if nums[index] % 2 == 0:
                sum_even += nums[index]
                
            
            answer.append(sum_even)

        return answer
