class Solution(object):
    def maxArea(self, height):
        lp = 0
        rp = len(height) - 1
        maxWater = 0
        
        while lp < rp:
            taller = min(height[lp], height[rp])
            maxWater = max(taller * (rp - lp), maxWater)
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        
        return maxWater