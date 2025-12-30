class Solution:
    def toHex(self, x: int) -> str:
        dict={}
        if x==0:
           return "0"
        bit=32
        for i in range(10,16):
             dict[i]=chr(ord("a")+i-10)    
        n=x&((1<<bit)-1)
        pq=""
        while n>0:
            if n%16<10:
                 pq=pq+str(n%16)
            else:
               pq=pq+dict[n%16]
            n//=16
        return ("".join(map(str,pq)))[::-1]      
