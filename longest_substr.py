#http://rosalind.info/problems/lcsm/
#http://stackoverflow.com/questions/2892931/longest-common-substring-from-more-than-two-strings-python
#http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python
#http://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/suffixtrees.pdf
from Bio import SeqIO

def get_fasta_records(file):
    fasta_seq=[]
    for seq_record in SeqIO.parse(file,"fasta"):
        s=str(seq_record.seq)
        fasta_seq.append(s)
    #print(fasta_seq)
    return fasta_seq


def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr
               
#s1='GATTACA'
#s2='TAGACCA'
#s3='ATACA'
file="rosalind_lcsm.txt"
data=get_fasta_records(file)
#print(data)
print(long_substr(data))
