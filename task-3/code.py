
# University Admission Decision Engine

applicants = []

n = int(input("Enter number of applicants: "))

subject_cutoff = float(input("Enter subject cutoff: "))
minimum_marks = float(input("Enter minimum aggregate marks: "))

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter name: ")
    subject = float(input("Enter subject marks: "))
    aggregate = float(input("Enter aggregate marks: "))
    entrance = float(input("Enter entrance marks: "))

    if subject >= subject_cutoff and aggregate >= minimum_marks:
        applicants.append([name, aggregate, subject, entrance])

# Sort using tie-breaking rules
applicants.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

# Display ranked list
print("\n--- ELIGIBLE APPLICANTS ---")

if len(applicants) == 0:
    print("No eligible applicants found.")
else:
    rank = 1

    for student in applicants:
        print("Rank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Subject Marks:", student[2])
        print("Entrance Marks:", student[3])
        print("--------------------")
        rank += 1

