# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        counterList = []
        while l1 or l2:
          x = l1.val if l1 else 0
          y = l2.val if l2 else 0
          sumXY = x + y
          if sumXY >= 10:
            sumXYCarry = int(carry + (sumXY % 10))
            if sumXYCarry == 10:
              counterList.append(0)
              carry = 1
            else:
              counterList.append(sumXYCarry)
              carry = sumXY/10
          else:
            sumXYCarry = int(carry + (sumXY))
            if sumXYCarry == 10:
              counterList.append(0)
              carry = 1
            else:
              counterList.append(sumXYCarry)
              carry = 0
          try:
            l1 = l1.next
          except:
            l1 = None
          try:
            l2 = l2.next
          except:
            l2 = None
        if carry != 0:
          counterList.append(int(carry))
        return counterList