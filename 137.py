def singlenumbers(nums):
     a = 0
     b = 0
     for x in nums:
         a = (a ^ x) & ~ b
         b = (b ^ x) & ~a
     return a
