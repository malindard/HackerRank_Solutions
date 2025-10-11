'''
Link: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
Difficulty: easy
Max score: 10
'''
if __name__ == '__main__':
    grades = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
        scores.append(score)
        
    scores = sorted(list(set(scores))) # remove duplicates + sort
    second_lowest = scores[1]
    names = []
    for name, score in grades:
        if score == second_lowest:
            names.append(name) # string
    for name in sorted(names):
        print(name)