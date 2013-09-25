#http://rosalind.info/problems/perm/
import itertools

def the_list(n):
   j=[]
   for i in range(1,n+1):
     j.append(i)
   return j

def perm(thelist):
   a=itertools.permutations(thelist)
   j=[]
   for item in a:
      j.append(item)
   perm_length=len(j)
   print(perm_length)
   return j

h=perm(the_list(7))
#print(h)
for item in h:
   g=' '.join(str(x) for x in item) 
   print(g)
