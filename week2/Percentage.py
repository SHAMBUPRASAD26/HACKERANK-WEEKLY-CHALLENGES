if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0
    score_len=0
    for name,score in student_marks.items():
        if name==query_name:
            score_len=len(score)
            for j in score:
                sum+=j
    avg=float(sum/score_len)
    print("{:.2f}".format(avg))            
                