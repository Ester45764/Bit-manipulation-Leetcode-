class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
      res=0
      while right>left:
         right>>=1
         left>>=1
         res+=1
      return  right<<res
