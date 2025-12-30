class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def bitcalculate(n):
            count=0
            while n:
               n=n&(n-1)
               count+=1
            return count            
        n=len(nums)
        prev=float('inf')
        prevmaximum=float('-inf') 
        prevstable=float('-inf')
        for i in range(n):
            if  prev!=bitcalculate(nums[i]): 
                  prev=bitcalculate(nums[i])  
                  prevmaximum=prevstable
                  prevstable=float('-inf')
            if prevmaximum> nums[i]:
                 return False 
            prevstable=max(nums[i],prevstable)
        return True     
