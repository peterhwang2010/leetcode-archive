class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      def mergeSort(arr):
        if len(arr) > 1:
          mid = len(arr) // 2
          left_array = arr[:mid]
          right_array = arr[mid:]
          mergeSort(left_array)
          mergeSort(right_array)
          
          l, r, m = 0, 0, 0
          
          while l < len(left_array) and r < len(right_array):
            if left_array[l] <= right_array[r]:
              arr[m] = left_array[l]
              l += 1
            else: 
              arr[m] = right_array[r]
              r += 1
            m += 1
          
          while l < len(left_array):
            arr[m] = left_array[l]
            l += 1
            m += 1
          
          while r < len(right_array):
            arr[m] = right_array[r]
            r += 1
            m += 1 

        return arr
      
      if len(intervals) < 2:
        return intervals
      intervals.sort(key=lambda x: x[0])
      return_intervals = []
      for index in range(len(intervals)):
        if index == 0:
          return_intervals.append(intervals[index])
        else:
          if return_intervals[-1][1] < intervals[index][0]:
            return_intervals.append(intervals[index])
          else:
            return_intervals[-1][1] = max(return_intervals[-1][1], intervals[index][1])
      return return_intervals
      