from collections import deque
class Solution:
    def lastRemaining(self, n: int) -> int:
        l_to_r = True
        remain = n
        step = 1
        first_num = 1
        while remain > 1:
            if l_to_r or remain % 2 != 0:
                first_num += step 
            remain //=2
            step *=2
            l_to_r = not l_to_r

        return first_num