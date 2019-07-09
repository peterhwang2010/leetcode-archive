class Solution:
  def romanToInt(self, s: str) -> int:
      symbol_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
      output_val = 0
      index = 0
      prev_val = 0
      if len(s) < 2:
        return output_val + symbol_dict[s[0]]
      
      for index in range(len(s)):
        if index == 0:
          prev_val = symbol_dict[s[index]]
        else:
          if symbol_dict[s[index]] <= prev_val:
            output_val += prev_val
            prev_val = symbol_dict[s[index]]
          else:
            prev_val = symbol_dict[s[index]] - prev_val
      return output_val + prev_val
            

