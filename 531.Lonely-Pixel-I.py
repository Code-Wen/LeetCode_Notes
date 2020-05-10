# 531. Lonely Pixel I

# Medium

# https://leetcode.com/problems/lonely-pixel-i/

# Given a picture consisting of black and white pixels, find the number of black lonely pixels.

# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

# A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n, cols = len(picture), len(picture[0]), collections.defaultdict(int)
        rows = []
        for i in range(m):
            count, col = 0, -1
            for j, l in enumerate(picture[i]):
                if  l == 'B':
                    count += 1
                    col = j
                    cols[col] += 1
            if count == 1: 
                rows.append((i, col))
        return len([1 for i, col in rows if cols[col]==1])
                