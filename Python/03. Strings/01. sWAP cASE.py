'''
Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
Difficulty: Easy
Max score: 10
'''

def swap_case(s):
    # solution start
    return s.swapcase()
    # solution end

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
