"""
http://rosalind.info/problems/perm/

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of
all such permutations (in any order).

"""
n = int(open('rosalind_perm.txt').read())
#print(n)

def get_number(n):
	if n == 1:
		number = 1
	else:
		number = n * (n - 1)
	return number

number = get_number(n)
print(number)