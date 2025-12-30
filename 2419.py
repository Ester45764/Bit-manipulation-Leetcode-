class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
            n=len(nums)
            maximum=max(nums)
            count=0 
            maxvalue=float('-inf')
            for i in range(n):
                if maximum==nums[i]:
                    count+=1
                else:
                     maxvalue=max(maxvalue,count)
                     count=0
            return max(maxvalue,count) 
