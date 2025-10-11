'''
We won't get expected result in Python 3 as Python 2 because it intentionally randomizes it for security, 
that means any solution using Python 3's hash() will produce a random number. Because there is a difference 
in Python 2's hash() and Python 3's hash().
Python 2's hash() : Deterministic hash
Python 3's hash() : Randomized hash

Link: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
Difficulty: easy
'''
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))