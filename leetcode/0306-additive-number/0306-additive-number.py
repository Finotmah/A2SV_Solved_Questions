class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(start,seq):
            if start == len(num) and len(seq) >= 3:
                return True
            
            for i in range(start, len(num)):

                if num[start] == '0' and i > start:
                    break
                
                next_num = int(num[start:i+1])

                if len(seq) >=2 and next_num != seq[-1] + seq[-2]:
                    continue
                
                seq.append(next_num)

                if backtrack(i+1,seq):
                    return True
                seq.pop()

            return False
        return backtrack(0,[])