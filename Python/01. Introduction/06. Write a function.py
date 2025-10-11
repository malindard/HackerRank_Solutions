'''
Link: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
Difficulty: Medium
Max score: 10
'''

# SOLUTION START
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap
# SOLUTION END

year = int(input())
print(is_leap(year))
