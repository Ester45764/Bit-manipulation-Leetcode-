class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
            pos=[0]*(32) 
            for i in range(len(candidates)):
                  for bit in range(32):
                       if candidates[i]&(1<<bit)>0:
                             pos[bit]+=1
            return  max(pos)
