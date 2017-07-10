'''
Problem

In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

Given: A protein string PP of length at most 1000 aa.

Return: The total weight of PP. Consult the monoisotopic mass table.
'''
def get_aa_weight_dict():
	inf = open('Monoisotopic_mass_table.txt')
	aa_mass_dict = {}
	aa = ''
	for line in inf:
		aa = line.strip().split()[0]
		aa_mass_dict[aa] = ''
		aa_mass_dict[aa] = line.strip().split()[1]
	inf.close()
	return aa_mass_dict


def get_protein_sequence():
	protein_sequence = open('data//rosalind_prtm.txt').read()
	#print(protein_sequence)
	return protein_sequence



def get_protein_weight(protein_sequence, aa_mass_dict):
	protein_weight = 0.0
	for aa in protein_sequence:
		if aa in aa_mass_dict:
			protein_weight += float(aa_mass_dict[aa])

	protein_weight -= 18.01056 #weight of one molecular water
	return protein_weight

aa_mass_dict = get_aa_weight_dict()
protein_sequence = get_protein_sequence()
print('the total mass of the protein is: %s kDa'% get_protein_weight(protein_sequence, aa_mass_dict))
