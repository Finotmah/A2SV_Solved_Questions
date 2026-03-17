class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        min_rabbit = 0

        mymap = {}

        for ans in answers:
            if ans == 0:
                min_rabbit += 1
            else:
                mymap[ans] = mymap.get(ans,0) + 1
                if mymap[ans] == ans + 1:
                    min_rabbit += ans + 1
                    del mymap[ans]
        for num in mymap:
            min_rabbit += num + 1


        return min_rabbit