sample = ['GTA','GGG','CAC']

"""This method will read the dna files and retrun a string which contain DNA data"""
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data

"""This method will take a string and create a list of codons from that string and return a list. it takes a string as input"""
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i+3) < len(dna):
      codons.append(dna[i:i+3])
  return codons

"""THis method will iterat through both the sample and a suspect's DNA and count the number of times a codon in the sample matches a codon in the suspect's DNA. it takes a list as input """
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches
"""This method will check if the suspect is criminal"""
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print ("%s is the number of matches. The investigation should continue" % num_matches)
  else:
    print ("%s is the number of matches. The suspect should be free" % num_matches)
    
is_criminal("suspect1.txt")    
is_criminal("suspect2.txt")    
is_criminal("suspect3.txt")    
