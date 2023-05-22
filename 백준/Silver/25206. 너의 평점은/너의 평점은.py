grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
total_score, total_grade = 0, 0
for _ in range(20):
    n, p, s = input().split()
    p = float(p)
    if s != 'P':
        total_score += p
        total_grade += p * score[grade.index(s)]
print(format(total_grade / total_score, '.6f'))
