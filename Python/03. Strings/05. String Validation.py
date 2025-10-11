'''
Link: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
Difficulty: Easy
Max score: 10
'''

def alphanum(s):
    for i in range(len(s)):
        if s[i].isalnum():
            return True;
            break;
    return False;
    
def alphabet(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return True;
            break;
    return False;
    
def digit(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True;
            break;
    return False;
    
def lower(s):
    for i in range(len(s)):
        if s[i].islower():
            return True;
            break;
    return False;
    
def upper(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True;
            break;
    return False;

if __name__ == '__main__':
    s = input()
    a = alphanum(s);
    b = alphabet(s);
    c = digit(s);
    d = lower(s);
    e = upper(s);
    print(a);
    print(b);
    print(c);
    print(d);
    print(e);
