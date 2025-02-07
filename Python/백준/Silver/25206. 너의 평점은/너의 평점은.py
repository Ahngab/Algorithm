grades = {"A+": 4.5, "A0":4.0, "B+":3.5, "B0": 3.0, "C+":2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
totalClass = 0
totalGrade = 0

for _ in range(20):
    temp = input().split()
    name, clas, grade = temp[0], temp[1], temp[2]
    if grade == "P":
        continue
    else:
        totalGrade += grades[grade]* float(clas)
        totalClass += float(clas)

print(totalGrade / totalClass)