class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = 0, 0, 0
        numstemp1 = nums1[:m]

        if len(nums2) == 0:
            return
        
        while i < m and j < n:
            if numstemp1[i] < nums2[j]:
                nums1[k] = numstemp1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        while i < m:
            nums1[k] = numstemp1[i]
            i += 1
            k += 1
            
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
