'''
Link: https://www.hackerrank.com/challenges/find-a-string/problem
Difficulty: Easy
Max score: 10
'''

#SOLUTION START
def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        # index variable will return the index where sub_string is
        index = string.find(sub_string)
        # we change the string where the index prefix of the previous string to go to the next index cuz we already found (one of) sub_string
        string = string[index+1:]
        # add count when find sub_string
        count+=1
    return count
#SOLUTION END

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
