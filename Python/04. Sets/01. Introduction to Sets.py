'''
Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
Difficulty: easy
'''
def average(array):
    # your code goes here
    arr = set(array)
    n = len(arr)
    return (sum(arr)/n) 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)