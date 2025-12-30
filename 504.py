class Solution:
    def convertToBase7(self, x: int) -> str:
       n=abs(x)
       if n==0:
            return "0"
       digit=""
       while n> 0 :
               digit=digit+str(n%7)
               n//=7
       return digit[::-1] if x>=0  else "-"+digit[::-1]
