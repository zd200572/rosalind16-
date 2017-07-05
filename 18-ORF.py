'''
================================
Open Reading Frames
================================
Problem

Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string ss of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of ss. Strings can be returned in any order.

Sample Dataset

>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
Sample Output

MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
'''
seq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

def get_rna_dict()
	rna_dict = {}
	for line in open('codons.txt').readlines():
		codon = line.strip().split()[0]
		#print(codon)
		if codon != '':
			rna_dict[codon] = line.strip().split()[1]
			#print(rna_dict[codon])
	return rna_dict


def transcipts(seq):
	mrna1 = ''
	mrna2 = ''
	for nucleotide in seq:
		if nucleotide == 'T':
			mrna1 += 'U':
		else:
			mrna1 += nucleotide
	dict = {A:U, T:A, G:C, C:G}
	for nucleotide in seq:
		for nucleotide in dict.keys():
			mrna2 += dict[nucleotide]
	return mrna1, mrna2


def 