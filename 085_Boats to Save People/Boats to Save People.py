class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        l = 0
        r = len(people)-1
        num_boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            num_boats += 1

        return num_boats


        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
