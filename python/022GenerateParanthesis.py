class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backTrace(s='', left=0, right=0):
          if len(s) == n*2:
            ans.append(s)
            return
          if left < n:
            backTrace(s + '(', left + 1, right)
          if right < left:
            backTrace(s + ')', left, right + 1)
        backTrace()
        return ans