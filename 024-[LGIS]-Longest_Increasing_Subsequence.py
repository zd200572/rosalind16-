'''
Problem

A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000n≤10000 followed by a permutation ππ of length nn.

Return: A longest increasing subsequence of ππ, followed by a longest decreasing subsequence of ππ.

Sample Dataset

5
5 1 4 2 3
Sample Output

1 2 3
5 4 2
Citationclick to collapse

Adapted from Jones & Pevzner, *An Introduction to Bioinformatics Algorithms, Problem 6.48.
'''

sequence = [5, 1, 4, 2, 3]

def get_subsequence(sequence):
    # We create arrays with 'n' positions and we start all of them with 'None'.
    m = [None] * len(sequence)
    permutations = [None] * len(sequence)

    # There is at least an increasing subsequence of length one, 
    # because it is the first element.
    last = 1
    
    # Stores the position of the lower or higher values, 
    # depending os the positions of the 'sequence'
    m[0] = 0

    for i in range(1, len(sequence)):
        # We want the largest j <= last
        #  such that sequence[m[j]] < sequence[i] (with default j = 0),
        #  hence we want the lower value.
        lower = 0
        upper = last

        # Verifying what is the upper value
        if sequence[m[upper - 1]] < sequence[i]:
            j = upper
        else:
            while (upper - lower) > 1:
                mid = (upper + lower) // 2
                if sequence[m[mid - 1]] < sequence[i]:
                    lower = mid
                else:
                    upper = mid
            
            # 'j' will also set the default value to 0.
            j = lower    

        permutations[i] = m[j - 1]

        if j == last or sequence[i] < sequence[m[j]]:
            m[j] = i
            last = max(last, j + 1)

    result = []
    pos = m[last - 1]
    
    # We use '_' when we don't want to use a variable into the loop.
    for _ in range(last):
        result.append(sequence[pos])
        pos = permutations[pos]

    return result[::-1]
    
#if __name__ == "__main__":
    #fid = open('rosalind_lgis.txt','r')
    
n = 5#int(fid.readline().strip())
#s = [int(x) for x in range(5)] #fid.readline().split()]
increasing = []
increasing = get_subsequence(sequence)
    
# We take the collection and revert the values.
# After the results, we revert again.
decreasing = []
decreasing = get_subsequence(sequence[::-1])[::-1]
    
print(str(increasing).strip('[]').replace(',',''))
print(str(decreasing).strip('[]').replace(',',''))

