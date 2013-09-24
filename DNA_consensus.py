from Bio import SeqIO

def get_fasta_records(file):
    fasta_seq=[]
    for seq_record in SeqIO.parse(file,"fasta"):
        s=str(seq_record.seq)
        fasta_seq.append(s)
    #print(fasta_seq)
    return fasta_seq

def seq_dict(s):
   seq_position_list=[]
   ACGT={'A':'','C':'','G':'','T':''}
   for key in ACGT:
      for i in range(0,len(s[0])):
         seq_position_list.append(0)
      ACGT[key]=seq_position_list
      seq_position_list=[]
   return ACGT

def seq_count(ACGT,s):
   ACGT_count=ACGT
   for seq in s:
      #print(seq)
      seq_index=0
      for seq_letter in seq:
         seq_list=ACGT_count[seq_letter]
         previous_seq_count=seq_list[seq_index]
         seq_count=previous_seq_count+1
         seq_list[seq_index]=seq_count
         ACGT_count[seq_letter]=seq_list
         seq_index+=1
   return ACGT_count

def consensus(ACGT_count):
#assesses the list associated with each key
#at the same position
#evaluates which key
#has the highest value
#(at that position)
#add key with highest value to consensus list
#moves to the next position
   position=0
   count=0
   consensus_seq=''
   seq_length=len(ACGT_count['A'])
   for position in range(0,seq_length):
      for letter in ACGT_count:
         seq_list=ACGT_count[letter]
         new_count=seq_list[position]
         if new_count>count:
            potential_consensus_letter=letter
            count=new_count
      consensus_seq+=potential_consensus_letter
      count=0
   #print(consensus_seq)
   return consensus_seq
     

#s="ATCCAGCT"
file="rosalind_cons.txt"
seqs=get_fasta_records(file)
#print(seqs)
a=seq_dict(seqs)
consensus_dictionary=seq_count(a,seqs)
print(consensus(consensus_dictionary))
for key in consensus_dictionary:
   g=' '.join(str(x) for x in consensus_dictionary[key])
   print(key+':',g)
