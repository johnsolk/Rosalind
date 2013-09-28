def prob_dom(list):
    AA_AA1=list[0]*2
    AA_Aa2=list[1]*2
    AA_aa3=list[2]*2
    Aa_Aa4=list[3]*2
    Aa_aa5=list[4]*2
    aa_aa6=list[5]*2
    #Probability that offspring will be dominant, 
    #Probability that offspring will be dominant, 
    offspringdominantphenotype=AA_AA1+AA_Aa2+AA_aa3+Aa_Aa4*0.75+Aa_aa5*0.5+aa_aa6*0
    return offspringdominantphenotype

list=[19504,18926,18529,18778,17697,17027]
print(prob_dom(list))
