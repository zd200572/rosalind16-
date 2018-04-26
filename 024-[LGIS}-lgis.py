sequence = [5, 1, 4, 2, 3]

def get_lgis(sequence):
	m = [None] * len(sequence)
	permutaion = [None] * len(sequence)
	left = 0
	right = last

	for i in range(1, len(sequence)):
		if sequence[m[left]] < sequence[i]
