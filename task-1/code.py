#university scholarship allocation
n = int(input("Enter number of students: "))

eligible = []

for i in range(n):
    print("\nEnter student details")

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))

    subjects = list(map(int, input(
        "Enter 3 subject marks: ").split()))

    attendance = float(input("Enter attendance: "))
    income = int(input("Enter family income: "))

    if (marks >= 75 and min(subjects) >= 60
        and attendance >= 75 and income <= 250000):

        eligible.append((name, marks, attendance, income))

    else:
        print(name, "is Not Eligible")

# Ranking students
eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\nScholarship Ranking")

for i, student in enumerate(eligible, 1):
    print(i, student)
