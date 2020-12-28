def dna_to_rna(dna):
    d={'A':'U','T':'A','G':'C','C':'G'}
    return ''.join([d[i] if i in d.keys() else i for i in dna])

a=dna_to_rna("CGATATA")
print(a)