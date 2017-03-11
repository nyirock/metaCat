import khmer
from Bio import SeqIO

fasta_sequences = SeqIO.parse(open("/home/andriy/canopy/scripts/metaCat/filtered_e_1e-05_iden95.0_alen50.0recruited_mg0.fasta"),'fasta')
dicts={}
for fasta in fasta_sequences:
    name, sequence = fasta.id, fasta.seq.tostring()
    ktable = khmer.new_ktable(6)
    ktable.consume(sequence)
    d={ktable.reverse_hash(i): ktable.get(i) for i in range(0,ktable.n_entries())}
    dicts[name]=d
# make a new ktable, L=6
count=0
for key,value in dicts.items():
    if value < 5:
        print key, value


# count all k-mers in the given string


# run through all entries. if they have nonzero presence, print.
#for i in range(0, ktable.n_entries()):
#   n = ktable.get(i)
#   if n:
#      print ktable.reverse_hash(i), "is present", n, "times."
#print dir(ktable)
