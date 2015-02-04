'''
Created on Feb 4, 2015

@author: Ian McPherson
'''

'''
 Iterates through the list and converts the DNA sequence to a RNA sequence.
'''
def DNAToRNA(list):
    RNA = []
    for i in range(len(list)):
        if list[i] == 'A':
            RNA.append('U')
            
        elif list[i] == 'T':
            RNA.append('A')
            
        elif list[i] == 'C':
            RNA.append('G')
            
        elif list[i] == 'G':
            RNA.append('C')
            
    return RNA

'''
 Iterates through the list and converts the RNA sequence to a DNA sequence.
'''
def RNAToDNA(list):
    DNA = []
    
    for i in range(len(list)):
        if list[i] == 'A':
            DNA.append('T')
            
        elif list[i] == 'U':
            DNA.append('A')
            
        elif list[i] == 'C':
            DNA.append('G')
            
        elif list[i] == 'G':
            DNA.append('C')
            
    return DNA

'''
 Iterates through the RNA sequence and creates codons. Then it checks the amino
 acid dictionary for the corresponding codon. It does this until the protein has
 been fully built.
'''
def RNAToProtien(list):
    amino = dict([('UUU', 'F'), ('UUC', 'F'), ('UUA', 'L'), ('UUG', 'L'), ('UCU', 'S'),
          ('UCC', 'S'), ('UCA', 'S'), ('UCG', 'S'), ('UAU', 'Y'), ('UAC', 'Y'),
          ('UAA', '*'), ('UAG', '*'), ('UGU', 'C'), ('UGC', 'C'), ('UGA', '*'),
          ('UGG', 'W'), ('CUU', 'L'), ('CUC', 'L'), ('CUA', 'L'), ('CUG', 'L'),
          ('CCU', 'P'), ('CCC', 'P'), ('CCA', 'P'), ('CCG', 'P'), ('CAU', 'H'),
          ('CAC', 'H'), ('CAA', 'Q'), ('CAG', 'Q'), ('CGU', 'R'), ('CGC', 'R'),
          ('CGA', 'R'), ('CGG', 'R'), ('AUU', 'I'), ('AUC', 'I'), ('AUA', 'I'),
          ('AUG', 'M'), ('ACU', 'T'), ('ACC', 'T'), ('ACA', 'T'), ('ACG', 'T'),
          ('AAU', 'N'), ('AAC', 'N'), ('AAA', 'K'), ('AAG', 'K'), ('AGU', 'S'),
          ('AGC', 'S'), ('AGA', 'R'), ('AGG', 'R'), ('GUU', 'V'), ('GUC', 'V'),
          ('GUA', 'V'), ('GUG', 'V'), ('GCU', 'A'), ('GCC', 'A'), ('GCA', 'A'),
          ('GCG', 'A'), ('GAU', 'D'), ('GAC', 'D'), ('GAA', 'E'), ('GAG', 'E'),
          ('GGU', 'G'), ('GGC', 'G'), ('GGA', 'G'), ('GGG', 'G')])
    protien = []
    counter = 0
    codon = []
    
    for i in range(len(list)):
        if counter == 3:
            counter = 0
            protien.append(amino[codon])
            codon = []
            
        codon.append(list[i])
        counter = counter + 1
        
    if counter == 3:
        protien.append(amino[codon])
        
    return protien
    
