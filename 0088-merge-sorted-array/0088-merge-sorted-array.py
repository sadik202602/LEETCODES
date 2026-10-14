class Solution(object):
    def merge(self, nums1, m, nums2, n):


      for s in range(n):
          nums1[m+s] = nums2[s]

      nums1.sort()
        