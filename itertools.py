"""
You are given a function f(X) = X**2. You are also given K lists. The ith list consists 
of N elements. You have to pick one element from each list so that the value from the equation below 
is maximized: 
S = (f(X1) + f(X2) + ... + f(X(k)))%M
X(i) denotes the element picked from the ith list . Find the maximized value S(max) obtained.
Note that you need to take exactly one element from each list, not necessarily the largest 
element. You add the squares of the chosen elements and perform the modulo operation. 
The maximum value that you can obtain, will be the answer to the problem.
Input Format
The first line contains 2 space separated integers K and M. 
The next K lines each contains an integer N(i), denoting the number of elements in the ith list, 
followed by N(i) space separated integers denoting the elements in the list.
Output Format
Output a single integer denoting the value S(max).
Sample Input
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output
206
"""
from itertools import product
k,m = map(int,input().split())
arr = (list(map(int, input().split()))[1:] for _ in range(k))
print(max(map(lambda x: sum(i**2 for i in x)%m, product(*arr))))

'''PRODUCT'''
from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*list(product(a,b)))

'''PERMUTATIONS'''
from itertools import permutations
s,k = input().split()
result = list(permutations(s,int(k)))
for i in sorted(result):
    for x in i:
        print(x,end='')
    print()

'''COMBINATIONS'''
from itertools import combinations
s, k = input().split()
for i in range(1,int(k)+1):
    for j in combinations(sorted(s),i):
        print(''.join(j))

'''COMBINATIONS WITH REPLACEMENT'''
from itertools import combinations_with_replacement
s,k = input().split()
for i in combinations_with_replacement(sorted(s),int(k)):
    print("".join(i))

'''COMPRESS THE STRING'''
from itertools import groupby
s = input()
print(*[(len(list(g)),int(k))for k,g in groupby(s)])
