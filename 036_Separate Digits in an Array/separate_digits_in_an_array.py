
class Solution(object):
    def separateDigits(self, nums):
        nums_digit = []

        for num in nums:
            if num == 0:
                nums_digit.append(0)
            digits = []
            while num > 0:
                digit = num % 10
                digits.append(digit)
                num = num // 10
            digits.reverse()
            nums_digit.extend((digits))

        return nums_digit
