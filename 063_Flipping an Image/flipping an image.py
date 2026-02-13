class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])

        
        for row in image:
            row.reverse()
        
        for i in range(rows):
            for j in range(cols):
                if image[i][j] == 0:
                    image[i][j] = 1
                    
                elif image[i][j] == 1:
                    image[i][j] = 0
        
        return image
