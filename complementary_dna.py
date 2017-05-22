#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complementary DNA
#Problem level: 7 kyu

dna_c = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
def DNA_strand(dna):
    return ''.join(dna_c[x] for x in dna)
