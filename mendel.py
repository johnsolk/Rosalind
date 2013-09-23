def prob_dom(k,m,n):
    total=k+m+n
    homo_dom1=k/total
    homo_dom2=k/(total-1)
    homo_dom3=(k-1)/(total-1)
    hetero_dom1=m/total
    hetero_dom2=m/(total-1)
    hetero_dom3=(m-1)/(total-1)
    homo_rec1=n/total
    homo_rec2=n/(total-1)
    outcome1=homo_dom1*homo_dom3
    outcome2=homo_dom1*hetero_dom2
    outcome3=homo_dom1*homo_rec2
    outcome4=hetero_dom1*homo_dom2
    outcome5=hetero_dom1*hetero_dom3
    outcome6=hetero_dom1*homo_rec2
    outcome7=homo_rec1*homo_dom2
    outcome8=homo_rec1*hetero_dom2
    #Probability that offspring will be dominant, 
    parentshomozygouscarriers=outcome1+outcome2+outcome3+outcome4+(outcome5*0.75)+(outcome6*0.5)+outcome7+(0.5*outcome8)
    return parentshomozygouscarriers
      
print(prob_dom(24,19,25))
    
