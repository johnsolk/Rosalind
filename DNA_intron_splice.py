#http://rosalind.info/problems/splc/
from Bio import SeqIO

def get_fasta_records(file):
    fasta_seq=[]
    for seq_record in SeqIO.parse(file,"fasta"):
        s=str(seq_record.seq)
        fasta_seq.append(s)
    #print(fasta_seq)
    return fasta_seq

def transcribe(DNA):
    RNA=DNA.replace('T','U')
    #print(RNA)
    return RNA

def motif_finder(sequence,intron):
#find first letter of sequence
#find first letter of intron
#compare
#if match, then, record beginning position on sequence
#then go to second letter of intron
#go to second letter of sequence
#compare
#if match, then continue
#if not, move to second letter of secuence, first letter of intron
#etc. until there is a total match
#finally, cut the sequence at that location until the end of the intron
#and splice the ends together
    #print('Intron',intron)
    #print(sequence)
    sequence_position=0
    beginning_sequence_position=0
    intron_position=0
    sequence_length=len(sequence)
    intron_length=len(intron)
    motif=''
    new_sequence=''
    while new_sequence=='':
        intron_letter=intron[intron_position]
        sequence_letter=sequence[sequence_position]
        if intron_letter==sequence_letter:
            motif+=sequence_letter
            #print(motif)
            u=intron_position+1
            if u<intron_length:
                intron_position+=1
                #print(intron_position)
            else:
                intron_position=0
            sequence_position+=1
        else:
            intron_position=0
            b=beginning_sequence_position+1
            sequence_position=b
            beginning_sequence_position=b
            motif=''
        if motif==intron:
            #print('Found motif',motif)
            sequence1=sequence[:beginning_sequence_position]
            c=beginning_sequence_position+intron_length
            sequence2=sequence[c:]
            new_sequence=sequence1+sequence2
            #print(new_sequence)
    return new_sequence

def aminoacid_codons():
#http://en.wikipedia.org/wiki/Genetic_code#RNA_codon_table
#http://www.cbs.dtu.dk/courses/27619/codon.html
#http://www.biochem.ucl.ac.uk/bsm/dbbrowser/c32/aacode.html
#http://www.biochem.ucl.ac.uk/bsm/dbbrowser/c32/aastruct.html
    aa={'UUU':'F','UUC':'F',\
        'UUA':'L','UUG':'L',\
        'UCU':'S','UCC':'S','UCA':'S','UCG':'S',\
        'UAU':'Y','UAC':'Y',\
        'UAA':'X','UAG':'X','UGA':'X',\
        'UGU':'C','UGC':'C',\
        'UGG':'W',\
        'CUU':'L','CUC':'L','CUA':'L','CUG':'L',\
        'CCU':'P','CCC':'P','CCA':'P','CCG':'P',\
        'CAU':'H','CAC':'H',\
        'CAA':'Q','CAG':'Q',\
        'CGU':'R','CGC':'R','CGA':'R','CGG':'R',\
        'AUU':'I','AUC':'I','AUA':'I',\
        'AUG':'M',\
        'ACU':'T','ACC':'T','ACA':'T','ACG':'T',\
        'AAU':'N','AAC':'N',\
        'AAA':'K','AAG':'K',\
        'AGU':'S','AGC':'S',\
        'AGA':'R','AGG':'R',\
        'GUU':'V','GUC':'V','GUA':'V','GUG':'V',\
        'GCU':'A','GCC':'A','GCA':'A','GCG':'A',\
        'GAU':'D','GAC':'D',\
        'GAA':'E','GAG':'E',\
        'GGU':'G','GGC':'G','GGA':'G','GGG':'G'}
    #I=Isoleucine
    #L=Leucine
    #V=Valine
    #F=Phenylalanine
    #M=Methionine=START
    #C=Cysteine
    #A=Alanine
    #G=Glycine
    #P=Proline
    #T=Threonine
    #S=Serine
    #Y=Tyrosine
    #W=Tryptophan
    #Q=Glutamine
    #N=Asparagine
    #H=Histidine
    #E=Glutamic acid
    #D=Aspartic acid
    #K=Lysine
    #R=Arginine
    #X=STOP
    return aa

def codon(RNA):
#http://bioweb.uwlax.edu/genweb/molecular/seq_anal/translation/translation.html
    codons=[]
    #print(RNA_seq)
    while RNA!='':
        a=RNA[0:3]
        codons.append(a)
        #print(a)
        RNA=RNA[3:]
    #print(codons)
    return codons

def translation(aa, RNA_ORF):
    SLC=[]
    for codon in RNA_ORF:
        if len(codon)==3:
            if aa[codon]!='X':
                SLC.append(aa[codon]) 
    protein=''.join(SLC)
    #print(protein)
    return protein

file="rosalind_splc.txt"
d=get_fasta_records(file)
sequence=d[0]
#print(sequence)
introns=d[1:]
a=len(introns)
#print(a)
for i in range(0,a):
    intron=introns[i]
    x=motif_finder(sequence,intron)
    #print(x)
    sequence=x
#print(sequence)


e=transcribe(sequence)
#print(e)
RNA_ORF=codon(e)
#print(RNA_ORF)
o=translation(aminoacid_codons(),RNA_ORF)
print(o)
