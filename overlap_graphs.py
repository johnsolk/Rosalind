#http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc11
from Bio import SeqIO

def seq_records(file):
    seq_dict={}
    for seq_record in SeqIO.parse(file,"fasta"):
        sequence=str(seq_record.seq)
        seq_dict[sequence]=seq_record.id
    #print(seq_dict)
    return seq_dict

def motif_O_k(suffix,prefix):
#finds a consensus motif
#between the suffix of one sequence
#and the prefix of the other sequence
    k=3
    motif1=suffix[-k:]
    motif2=prefix[:k]
    if motif1==motif2:
       return (suffix,prefix)
    return None

#seq_dictionary={'Rosalind_2323': 'TTTTCCC', \
#                'Rosalind_2391': 'AAATTTT', \
#                'Rosalind_5013': 'GGGTGGG', \
#                'Rosalind_0442': 'AAATCCC', \
#                'Rosalind_0498': 'AAATAAA'}
#seq_dictionary2 = {y:x for x,y in seqs.items()}


file="rosalind_grph.txt"
seqs=seq_records(file)
list1=[]
for key in seqs:
    list1.append(key)
#print(list1)

#n records, there are n-1 combinations of tests
#take the first record, compare it to all the others
#second record, compare it to all the others
    
answer_list=[]
for i in list1:
    for j in list1:
        if i!=j:
            ret=motif_O_k(i,j)
            if ret:
                answer_list.append(ret)
#print(answer_list)

for item in answer_list:
   suffix=str(item[0])
   prefix=str(item[1])
   print(seqs[suffix],seqs[prefix]) 







          
