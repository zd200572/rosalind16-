'''
Problem

Assume that an alphabet AA has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak)A=(a1,a2,…,ak), where a1<a2<⋯<aka1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z)(A,B,…,Z).

Given two strings ss and tt having the same length nn, we say that ss precedes tt in the lexicographic order (and write s<Lexts<Lext) if the first symbol s[j]s[j] that doesn't match t[j]t[j] satisfies sj<tjsj<tj in AA.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer nn (n≤10n≤10).

Return: All strings of length nn that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

Sample Dataset

A C G T
2
Sample Output

AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
'''
from itertools import product

def get_char_and_N():
	inf = open('data//rosalind_lexf.txt')
	list = []
	data = inf.readlines()
	N = 0
	N = int(data[1].strip())
	list = data[0].split()
	#print(list, '\n', N)
	return list, N
 

list, N = get_char_and_N()
#table = dict((c, i) for i, c in enumerate(list))
#print(table)

k_mers = [''.join(item) for item in product(list, repeat=N)]
print(k_mers)






