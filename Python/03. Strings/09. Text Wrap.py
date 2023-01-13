'''
Link: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
Difficulty: Easy
Max score: 10
'''

import textwrap

#SOLUTION START
def wrap(string, max_width):
    result = textwrap.fill(string, max_width)
    return result
#SOLUTION END

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
''' 
textwrap module have some methods. at first i try to use fill() method. the result is correct but it form a list. what we need is a string. so i use fill() method 
which return a string instead a list. there's also a method called shorten(). After shortening the string, the length of the text will be same as the specified width. 
It will add […] at the end of the string.
result = textwrap.fill(text=string, width=max_width)

link : https://www.tutorialspoint.com/python-text-wrapping-and-filling#:~:text=In%20python%20the%20textwrap%20module,textwrap%20module%20in%20our%20code.&text=Sr.No.
'''
