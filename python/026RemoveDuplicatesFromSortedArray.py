class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      if len(nums) < 2:
        return
      index = 0
      while index < len(nums) - 1:
        if nums[index] == nums[index + 1]:
          del nums[index]
        else:
          index += 1
      
      if len(nums) > 1 and nums[-1] == nums[-2]:
        del nums[-1]
        