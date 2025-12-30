class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        prefix=[0]*(n+1)
        for i in range(n): 
            prefix[i+1]=prefix[i]^arr[i]
        print(prefix[n])
        count=0 
        for i in range(n):
              for j in range(i+1,n):
                    if (prefix[j+1]^prefix[i]==0) :
                          count+=j-i
        return count
