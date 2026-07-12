class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        # setting up right/left highest
        left_highest = [height[0]]
        right_highest = [height[-1]]
        # and filling them
        for l in range(1, len(height)):
            r = len(height)-1 - l
            left_highest.append(max(left_highest[-1], height[l]))
            right_highest.insert(0, max(right_highest[0], height[r]))
        
        # calculating area
        for i in range(1, len(height)):
            area += min(left_highest[i], right_highest[i]) - height[i]
        
        return area
