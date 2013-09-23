#http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc11
from decimal import *
from Bio import SeqIO

def seq_count(s):
    ACGT={'A':0,'C':0,'G':0,'T':0}
    for seq_letter in s:
        ACGT[seq_letter]+=1
    #print(ACGT['A'],ACGT['C'],ACGT['G'],ACGT['T'])
    return ACGT

def GCcontent(ACGT):
#((G+C)/(A+T+G+C))*100 (http://en.wikipedia.org/wiki/GC-content)"""
    GCfloat=((ACGT['G']+ACGT['C'])/(ACGT['A']+ACGT['T']+ACGT['G']+ACGT['C']))*100
    #print(ACGT)
    #print('GCfloat',GCfloat)
    GC=Decimal(GCfloat).quantize(Decimal('0.0000001'), rounding=ROUND_UP)
    #print('GC',GC)
    return GC

#f=open("rosalind_gc.txt")
#print(f.read().strip())
maxGCpercent=0
for seq_record in SeqIO.parse("rosalind_gc.txt","fasta"):
    s=seq_record.seq
    #print(len(seq_record))
    GC=GCcontent(seq_count(s))
    if GC>maxGCpercent:
        maxGCid=seq_record.id
        maxGCpercent=GC
print(maxGCid)
print(maxGCpercent)

          
#s='TGCCTGGTGTCACGCTGTGCAGACTGCCCTTTCGACCTTCCCGGGCCGCACGATACAGTACCCAACAATTGTCACTATCTACTATCGCCGGCATCCGCTGCGCGAGGGTAGTTTTGTAGGTCCATTGTACCCCTTTTTGCCCTTATCTGTGTTTGAGGTCGCGCCATCAAGGGTCGTCCTGTCCGCCCTCACCAGGGCTGATTGATCTTACTGGTACACTATCGCGTTTACAGTTTACGCCAGAACAACTCGTTGGGAAGTGGTGTCGACTGAGCTCTCTTCATCTCATGCCACCCGCGTATAACGCACTAAAGAGTGTGCGAGGAAATGTGATAGAGCCTCATGACCATAAACGCAAATAAACTTAGCGCACGTCTGACACCTCATCTATTGCCGATGTGGCAGGCGATAGTATAACCGCTTAGTTGTACTTTTTATATTGATTGTCCCGAGACCGCATACTATTACGTAAGTATGAAAGGGGACCTGTAGGTCGCCTTATTCAACTGGGGCACCCCGTGTTGAGGGAACTATCCGCTAGGGGAACCAGCCGGTTGTCGCAGATTTTGTGTATAAGTATATCGTAACAGCTCACTCTTATAATTAATCGGAAATTGAAACCGTGGCTACTGGTATCTCCTGACGTCATTGCAAGATCAAGATTGAAGGCTCAGAAAAGTTTTTGACCCTCGTGGGTGGGGCGTATGCATGACCCATTCGTGGCGCCCAGCCGGGAGGTACTATTCCGGTGCGAATATATGATGTGAAGATGTATGCAGGTTGAACTTCAGTCTCCCCCTAAGGCACGTACCCGAAATAAATGGTGATGAGTAATTAACATTC'
#print(GCcontent(seq_count(s)))
#s='AGCTATAG'
#print(GCcontent(seq_count(s)))
