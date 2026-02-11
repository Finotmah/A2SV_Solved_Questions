class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        count = dict()
        max_frq = 0
        common_res = ""

        for response in responses:
            day_response = set(response)
            for res in day_response:
                
                count[res] = count.get(res,0) + 1
                if max_frq == 0:
                    max_frq = 1
                    common_res = res
                    
                if count[res] == max_frq and res < common_res:
                    common_res = res

                elif count[res] > max_frq:
                    common_res = res
                max_frq = max(max_frq, count[res])

        return common_res

