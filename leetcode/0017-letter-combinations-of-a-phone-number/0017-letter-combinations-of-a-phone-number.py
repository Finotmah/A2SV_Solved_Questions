class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, path):
            if len(path) == len(digits):
                res.append(path)
                return

            for c in phone[digits[i]]:
                backtrack(i + 1, path + c)

        backtrack(0, "")
        return res