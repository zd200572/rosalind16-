'''
Problem

After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string ss (of length at most 1 kbp) and a collection of substrings of ss acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of ss. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset

>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
Sample Output

MVYIADKQHVASREAYGHMFKVCA
'''
def cut_introns(dna, introns):
	'''cut the sequence of introns'''
	for intron in introns:
		dna = dna.replace(intron, '')
	'''
	for intron in introns:
		#print(intron)
		in_length = len(intron)
		for i in range(len(dna) - in_length):
			#print(len(dna))
			if dna[i:i + in_length] == intron:
				#print(intron)
				dna = dna[:i] + dna[i + in_length:]
				#print(dna)'''
	print(dna)
	return dna

def transcipts(seq):
	mrna = ''
	dict = {'A':'U', 'T':'A', 'G':'C', 'C':'G'}
	for nucleotide in dict.keys() and seq:
			mrna += dict[nucleotide]
	#print(mrna)
	return mrna


def translate_rna_to_protein(mRNA):
	# Translating RNA into Protein
	codon_table = {
	    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
	    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
	    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
	    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
	    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
	    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
	    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
	    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
	    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
	    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
	    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
	    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
	    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
	    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
	    'UAC':'Y', 'UAU':'Y', 'UAA':'', 'UAG':'',
	    'UGC':'C', 'UGU':'C', 'UGA':'', 'UGG':'W',
	    }
	protein = ''
	i = 0
	g = 0
	for i in range(0, len(mRNA),3):
		if mRNA[i:i+3] in codon_table.keys():
			if mRNA[i:i+3] == 'AUG' and g != 1:
				print("tranlate starting:")
				protein += codon_table[mRNA[i:i+3]] 
				g = 1
			elif codon_table[mRNA[i:i+3]] == '':
				break
			elif g==1:
					protein += codon_table[mRNA[i:i+3]]

	print("The protein is :\n",protein)



def parse_fasta(filename):	
	dna = ''
	introns = []
	i = 0
	for a in open(filename):
		#print(a)
		#outf.write(a)
		#print(str(a)[2])
		if a[0] == '>' and dna == '':
			i = 1
		elif a[0] == '>':
			i = 0
		elif i == 1:
			dna += a.strip()
		else:
			introns.append(a.strip())
	print(len(dna))
	return dna, introns


#dna = ''
#introns = []
dna, introns = parse_fasta('data\\rosalind_splc.txt')
dna = cut_introns(dna, introns)
mRNA = transcipts(dna)
translate_rna_to_protein(mRNA)
