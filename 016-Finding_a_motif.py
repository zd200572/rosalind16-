'''
Problem Title: Finding a Protein Motif
Rosalind ID: MPRT
Rosalind #: 016
URL: http://rosalind.info/problems/mprt/
Motif Implies Functionclick to expand
Problem:
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.
You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into
http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following
http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
Sample Dataset:
B5ZC00
Sample Output
B5ZC00
85 118 142 306 395
'''
# To allow for the presence of its varying forms,
# a protein motif is represented by a shorthand as follows: 
# [XY] means "either X or Y" and {X} means "any amino acid except X." 
# For example, the N-glycosylation motif is written as N{P}[ST]{P}.
from urllib import request
import re

#此处还可以直接用Biopython中的ExPASy解决，代码见最后，参考自《Python生物信息学数据管理（Manaing your Biological Data with Python)》
def fetch_fasta_file(uniprot_id):
	url = 'http://www.uniprot.org/uniprot/' + uniprot_id + '.fasta'
	response = request.urlopen(url)
	file = response.readlines()
	#print(file)
	seq, seq_name = parse_fasta(file)
	return seq, seq_name

seq = ''
seq_name = ''
def parse_fasta(file):
	seq = ''
	seq_name = ''
	outf = ('%s.fasta' % uniprot_id, 'w')
	for a in file:
		#outf.write(a)
		#print(str(a)[2])
		if str(a)[2] == '>':
			seq_name = str(a)[3:len(a) - 2]
			#print(seq_name + '\n\n\n\n')
			
		else:
			seq += str(a)[2:len(a) - 2]
			#print(seq)
			#break
	#print(seq_name + '\n' + seq)
	return seq, seq_name


def search_motif(seq_name, sequence):
	#其中一个作者的方法
	#print(seq_name)
	'''
	for i in range(len(sequence) - 3):
		if sequence[i] != 'N':
			continue
		if sequence[i+1] == 'P':
			continue
		if sequence[i+2] not in ['S', 'T']:
			continue
		if sequence[i+3] == 'P':
			continue
		print(i, '\t')
		#yield i
		
'''
	#彩正则表达式
	pattern = re.compile('N[^P][ST][^P]')
	ite = pattern.finditer(sequence)

	if ite:
		print(seq_name)
		#print('\n')
		for s in ite:
			print(s.start(), end="")
			print('\t', end="")
			#print(s.end(), end="")
			#print('\t')
	else:
		print(seq_name, 'Not Founded the motif')




inf = open('in-016-rosalind_mprt.txt')
for line in inf:
	uniprot_id = line.strip()
	seq1, seq_name1 = fetch_fasta_file(uniprot_id)
	search_motif(seq_name1, seq1)
	break


#biopython

'''
from Bio import ExPASy
from Bio import SeqIO
handle = ExPASy.get_sprot_raw(uniprot_id)
seq_record = SeqIO.read(handle, "swiss")
out = open(uniprot_id + '.fasta','w')
fasta = SeqIO.write(seq_record, out, "fasta")
out.close()
'''