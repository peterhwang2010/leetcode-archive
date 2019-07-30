class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      for i in range(len(digits)):
        if digits[-(i + 1)] != 9:
          digits[-(i + 1)] += 1
          return digits
        else:
          if i + 1 < len(digits):
            digits[-(i + 1)] = 0
          else:
            digits[-(i + 1)] = 0
            digits = [1] + digits
            return digits
