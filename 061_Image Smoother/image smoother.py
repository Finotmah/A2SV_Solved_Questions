class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(img)
        cols = len(img[0])

        result = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                sums = img[i][j]
                count = 1
                if i + 1 < rows:
                    sums += img[i + 1][j]
                    count += 1
                if i - 1 >= 0:
                    sums += img[i - 1][j]
                    count += 1
                if j + 1 < cols:
                    sums += img[i][j + 1]
                    count += 1
                if j - 1 >= 0:
                    sums += img[i][j - 1]
                    count += 1
                if i + 1 < rows and j + 1 < cols:
                    sums += img[i + 1][j + 1]
                    count += 1
                if i - 1 >= 0 and j - 1 >= 0:
                    sums += img[i - 1][j - 1]
                    count += 1
                if i + 1 < rows and j - 1 >= 0:
                    sums += img[i + 1][j - 1]
                    count += 1
                if i - 1 >= 0 and j + 1 < cols:
                    sums += img[i - 1][j + 1]
                    count += 1
                    
                result[i][j] = sums//count
                

        return result
                
        
