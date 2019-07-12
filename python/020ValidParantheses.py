class Solution:
  def isValid(self, s: str) -> bool:
    tempList = []

    if len(s)%2 != 0:
      return False
    
    if len(s) == 0:
      return True

    for letter in s:
      if letter == '(' or letter == '[' or letter == '{':
        tempList.append(letter)
      else:
        if len(tempList) == 0:
          return False
        else:
          if letter == ')' and tempList[-1] == '(':
            tempList = tempList[:-1]
          elif letter == '}' and tempList[-1] == '{':
            tempList = tempList[:-1]
          elif letter == ']' and tempList[-1] == '[':
            tempList = tempList[:-1]
          else:
            return False
    
    if len(tempList) == 0:
      return True
    else:
      return False
      