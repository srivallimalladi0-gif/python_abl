n = int(input("Enter number of passengers: "))

total = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = int(input("Enter distance: "))

    print("1. Sleeper")
    print("2. AC")

    choice = int(input("Select class: "))

    if distance <= 100:
        fare = distance * 1

    elif distance <= 500:
        fare = distance * 1.5

    else:
        fare = distance * 2

    if choice == 1:
        fare = fare * 1

    elif choice == 2:
        fare = fare * 2

    else:
        print("Invalid class")
        continue

    if age >= 60:
        fare = fare * 0.8

    fare = fare + 50

    cancel = input("Cancel ticket? (yes/no): ")

    if cancel.lower() == "yes":
        penalty = fare * 0.25
        fare = fare - penalty

    print("Passenger Name:", name)
    print("Final Fare:", fare)

    total = total + fare

print("\n--- RAILWAY FARE SUMMARY ---")
print("Total Fare:", total)