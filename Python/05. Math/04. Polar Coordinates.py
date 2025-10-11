'''
Link: https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
Difficulty: easy
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase

z = complex(input())
print(abs(z))
print(phase(z))