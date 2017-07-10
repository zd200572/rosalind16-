'''
Problem

Figure 2. Palindromic recognition site
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset

>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
Sample Output

4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
'''
def read_fasta(filename):
	inf = open(filename)
	sequence = ''
	sequence_name = ''
	for line in inf:
		if line.startswith('>'):
			sequence_name = line.strip()[1:]
			#print(sequence_name)
		else:
			sequence +=line.strip().upper()
	#print(sequence)
	return sequence, sequence_name

'''###I have got the wrong idea 
def search_reverse_palindrome_seq(sequence, sequence_name):
	reverse_palindrome = ['GCATGC', 'CGTACG']
	reverse_palindrome_pos = []
	i = 0
	for i in range(len(sequence) - 6):
		if sequence[i:i + 6] in reverse_palindrome:
			reverse_palindrome_pos.append(i)
			print(i)
		return reverse_palindrome_pos

'''
def search_reverse_palindrome_seq(sequence, sequence_name):
	reverse_palindrome_pos = []
	reverse_palindrome_len = []
	for j in range(4, 13):
		for i in range(len(sequence) - j):
			if sequence[i:i+j] == reverse_compliment(sequence[i:i+j]):
				#print(sequence[i:i+j])
				reverse_palindrome_pos.append(i)
				reverse_palindrome_len.append(j)
	return reverse_palindrome_pos, reverse_palindrome_len


def reverse_compliment(seq):
	reverse_compliment = ''
	dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	for nucleotide in seq:
		if nucleotide in dict:
			reverse_compliment += dict[nucleotide]
	reverse_compliment = reverse_compliment[::-1]
	#print(reverse_compliment)
	return reverse_compliment



sequence, sequence_name = read_fasta('data//rosalind_revp.txt')
#sequence_name= 'Rosalind_24'
#sequence = 'TCAATGCATGCGGGTCTATATGCAT'
reverse_palindrome_pos, reverse_palindrome_len = search_reverse_palindrome_seq(sequence, sequence_name)
print(sequence_name)
for k in range(len(reverse_palindrome_pos)):
	print(reverse_palindrome_pos[k], reverse_palindrome_len[k])


