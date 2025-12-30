class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
       def searchxor(xor):
           for  bit  in range(32):
               if  xor&(1<<bit)!=0 : 
                      return bit
       n=len(nums)
       xor=0
       for i in range(n):
            xor=xor^nums[i]
       bit=searchxor(xor)
       xor1=0
       xor2=0
       for i in range(n):
           if nums[i]&(1<<bit)==0:
                   xor1=xor1^nums[i]
           else:
                 xor2=xor2^nums[i]
       return  [xor^xor1,xor^xor2]   
