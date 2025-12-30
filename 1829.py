class Solution:
    def getMaximumXor(self, nums: List[int], maximumbit: int) -> List[int]:
     xor=0     
     for elment in nums:
         xor^=elment
     maximum=(1<<maximumbit)-1 
     tab=[]
     tab.append(xor^maximum)
     for i in range(len(nums)-1,0,-1):
           xor^=nums[i]
           tab.append(xor^maximum)
     return tab
