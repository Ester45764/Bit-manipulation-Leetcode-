class Solution:
    def minEnd(self, n: int, x: int) -> int :
     res=x 
     add=n-1
     bit=0
     while add>0:
        if (x>>bit)&1==0:
            if (add&1)==1:
                   res=res|(1<<bit)
            add>>=1
        bit+=1
     return res
