class Solution:
    def maxArea(self, height: List[int]) -> int:
      maxArea = 0
      i = 0
      j = len(height) - 1
      while i < j:
        if height[i] < height[j]:
          area = height[i] * (j - i) 
          maxArea = area if area > maxArea else maxArea
          i += 1
        else:
          area = height[j] * (j - i) 
          maxArea = area if area > maxArea else maxArea
          j -= 1
      return maxArea