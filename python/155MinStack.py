class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def push(self, x: int) -> None:
      if len(self.data) == 0:
        self.data.append((x, x))
      else:
        self.data.append((x, min(x, self.data[-1][1])))
        

    def pop(self) -> None:
      self.data = self.data[:-1]
        

    def top(self) -> int:
      return self.data[-1][0]

    def getMin(self) -> int:
      return self.data[-1][1]
