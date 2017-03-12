from Bio import SeqIO
import pandas as pd
fasta_sequences = SeqIO.parse(open("/home/andriy/canopy/scripts/metaCat/filtered_e_1e-05_iden95.0_alen50.0recruited_mg0.fasta"),'fasta')
#dicts={}
cnt=0
dna=pd.DataFrame(columns=('Name', 'Sequence'))
for fasta in fasta_sequences:
    name, sequence = fasta.id, fasta.seq.tostring()
    dna.loc[cnt]=[name, sequence]
    #d={ktable.reverse_hash(i): ktable.get(i) for i in range(0,ktable.n_entries())}
    #dicts[name]=d
    cnt+=1
# make a new ktable, L=6
count=0
print dna


# count all k-mers in the given string


# run through all entries. if they have nonzero presence, print.
#for i in range(0, ktable.n_entries()):
#   n = ktable.get(i)
#   if n:
#      print ktable.reverse_hash(i), "is present", n, "times."
#print dir(ktable)
