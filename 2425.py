class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        def xor(nums):
           xorbitwiser=0
           for elment in nums:
             xorbitwiser^=elment
           return xorbitwiser
        n1=len(nums1)
        n2=len(nums2)
        xor1=xor(nums1)
        xor2=xor(nums2)
        if n1%2==n2%2==0:
              return 0
        if n1%2==n2%2==1 :
             return xor1^xor2
        if n1%2==0 and n2%2==1:
             return xor1
        if n1%2==1 and n2%2==0:
              return xor2
