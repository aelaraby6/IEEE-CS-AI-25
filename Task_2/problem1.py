if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        

scores = list(set([score for name, score in students]))
scores.sort()

low = scores[1]


finalStudents = [name for name, score in students if score == low]

finalStudents.sort()

for student in finalStudents:
    print(student)
