"""
Calculate the Hamming Distance between two DNA strands - https://exercism.io/tracks/python/exercises/hamming

Your body is made up of cells that contain DNA. Those cells regularly wear out and need replacing, which they achieve by dividing into daughter cells. 
In fact, the average human body experiences about 10 quadrillion cell divisions in a lifetime!
When cells divide, their DNA replicates too. Sometimes during this process mistakes happen and single pieces of DNA get encoded with the incorrect information. 
If we compare two strands of DNA and count the differences between them we can see how many mistakes occurred. This is known as the "Hamming Distance".
We read DNA using the letters C,A,G and T. Two strands might look like this:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
They have 7 differences, and therefore the Hamming Distance is 7.
The Hamming Distance is useful for lots of things in science, not just biology, so it's a nice phrase to be familiar with :)

Implementation notes
The Hamming distance is only defined for sequences of equal length, so an attempt to calculate it between sequences of different lengths should not work. 
The general handling of this situation (e.g., raising an exception vs returning a special value) may differ between languages.
"""

dna_seq_1 = "GAGCCTACTAACGGGAT"
dna_seq_2 = "CATCGTAATGACGGCCT"

assert len(dna_seq_1) == len(dna_seq_2), "The 2 DNA sequence don't have the same length"


# 1st solution 
i, diff = 0, 0
for i in range(len(dna_seq_2) - 1):
    if dna_seq_1[i] != dna_seq_2[i]:
        diff += 1
    i += 1
print(f'the Hamming Distance is {diff}')


# 2nd solution 
diff = 0
for (i, letter) in enumerate(dna_seq_1):
    if letter != dna_seq_2[i]:
        diff += 1
print(f'the Hamming Distance is {diff}')

# 3rd solution 
diff = 0
for i, j in list(zip(dna_seq_1, dna_seq_2)):
    if i != j: diff += 1
print(f'the Hamming Distance is {diff}')