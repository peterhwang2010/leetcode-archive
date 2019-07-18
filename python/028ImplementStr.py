class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      index = 0
      haystackList = list(haystack)
      needleList = list(needle)
      if haystack == needle or needle == "":
        return 0
      if len(needleList) > len(haystackList) or len(needleList) < 1:
        return -1
      while index <= (len(haystackList) - len(needleList)):
        print(haystackList[index: index + len(needleList)])
        if haystackList[index: index + len(needleList)] == needleList:
          return index
        if index == len(haystackList) - len(needleList):
          return -1
        index += 1