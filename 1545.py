class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def f(s):
           k=""
           for i in range(len(s)):
                if s[i]=="1": 
                   k+="0"
                else:
                    k+="1"
           return k
        def iterative(n,k):
            precedent="0"
            while n>0:
                precedent=precedent+"1"+f(precedent)[::-1]
                n-=1
            return precedent[k]
        return iterative(n-1,k-1)
