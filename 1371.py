def findthelongestsubstrincontain(s):
       dict={'a':0,'e':1,'i':2,'o':3,'u':4}
       state=0
       freq={state:-1}
       n=len(s)
       ans=0
       for i in range(n):
           if s[i] in dict:
             state =state^(1<<dict[s[i]])
           if state in freq:
              ans=max(ans,i-freq[state])
           else:
               freq[state]=i
       return ans
