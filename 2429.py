class Solution:
    def minimizeXor(self, nums1: int, nums2: int) -> int:
        def countnumber1(n):
           count=0
           while n:
              n=n&(n-1)
              count+=1
           return count
        count= countnumber1(nums2)
        mask=0
        for i in range(33,-1,-1):
             if nums1&(1<<i)!=0 and count>0:
                mask=mask|(1<<i)
                count-=1
        if count>0:
            for  i in range(33):
                 if mask&(1<<i)==0 and count>0:
                    mask=mask|(1<<i)
                    count-=1                 
        return mask
