########################################
#Genome Assembly as Shortest Superstring
#########################################

def assemble_genome(list):
	assemble_genome = list[0]
	#print(assemble_genome)
	for a in list[1:]:
		lcs = ''
		lcs = longest_common_substring(assemble_genome, a)
		if a[:len(lcs)] = lcs or a[-len(lcs):] = lcs:
			print(lcs)
		else:
			for b in list[1:].
		if assemble_genome[:2] == lcs[-2:]:
			print('yes1')
			assemble_genome = a[:len(a) - len(lcs)] + assemble_genome
			#print(assemble_genome)
			#break
		if assemble_genome[-2:] == lcs[:2]:
			print('yes2')
			assemble_genome += a[len(lcs):]
			#print(assemble_genome)
			#break
	return assemble_genome

def longest_common_substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
   longest, x_longest = 0, 0
   for x in range(1, 1 + len(s1)):
       for y in range(1, 1 + len(s2)):
           if s1[x - 1] == s2[y - 1]:
               m[x][y] = m[x - 1][y - 1] + 1
               if m[x][y] > longest:
                   longest = m[x][y]
                   x_longest = x
           else:
               m[x][y] = 0
   return s1[x_longest - longest: x_longest]


def read_fasta(filename):
	inf = open(filename)
	sequence = []
	sequence_name = ''
	for line in inf:
		if line.startswith('>'):
			sequence_name = line.strip()[1:]
			#print(sequence_name)
		else:
			sequence.append(line.strip().upper())
	#print(sequence)
	return sequence


if __name__ == '__main__':

	#list = read_fasta('data/rosalind_long.txt')
	list = ['ATTAGACCTG', 'CCTGCCGGAA', 'AGACCTGCCG', 'GCCGGAATAC']
	#print(list)
	super_string = assemble_genome(list)
	print(super_string)