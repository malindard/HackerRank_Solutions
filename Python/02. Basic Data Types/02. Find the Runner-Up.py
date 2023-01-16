'''
Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
Difficulty: easy
Max score: 10
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr1 = list(set(arr))    # arr1 variable contain array that doesn't have iterable value and then change it into a list
    print(sorted(arr1)[-2])  # sorted arr1 then choose the second maximum value
    
'''
set() : method is used to convert any of the iterable to sequence of iterable elements with distinct elements
sorted() : creates a new sequence type containing a sorted version of the given sequence
'''
