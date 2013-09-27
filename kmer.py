#http://rosalind.info/problems/lexf/
import itertools

import itertools
s="A K M G"
n=4
g=s.replace(" ","")
j=[''.join(x) for x in itertools.product(g, repeat=n)]
#print(j)
for item in j:
   y=''.join(str(x) for x in item)
   print(y)
