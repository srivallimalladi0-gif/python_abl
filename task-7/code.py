
total_fine = 0
disqualification = 0

n = int(input("Enter number of violations: "))

for i in range(n):

    print("\nViolation", i + 1)

    vehicle = input("Enter vehicle category: ")

    print("1. Helmet Violation")
    print("2. Overspeeding")
    print("3. No Driving License")

    choice = int(input("Enter offence type: "))

    if choice == 1:
        fine = 500

    elif choice == 2:
        fine = 1000

    elif choice == 3:
        fine = 5000
        disqualification += 1

    else:
        print("Invalid Offence")
        continue

    repeat = input("Is it a repeat offence? (yes/no): ")

    if repeat.lower() == "yes":
        fine = fine * 1.5

    print("Vehicle Category:", vehicle)
    print("Final Fine: Rs.", fine)

    total_fine += fine

print("\n--- TRAFFIC PENALTY SUMMARY ---")

print("Total Fine: Rs.", total_fine)

if disqualification > 0:
    print("Disqualification Condition Identified")
else:
    print("No Disqualification Condition")