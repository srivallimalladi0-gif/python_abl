

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdrawal")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid Amount")
        rejected += 1

    elif choice == 1:
        balance += amount
        successful += 1
        print("Deposit Successful")

    elif choice == 2:
        if amount > 2000:
            print("Withdrawal Limit Exceeded")
            rejected += 1

        elif amount > balance:
            print("Insufficient Balance")
            rejected += 1

        else:
            balance -= amount
            successful += 1
            print("Withdrawal Successful")

    else:
        print("Invalid Transaction Type")
        rejected += 1

print("\n--- ATM TRANSACTION SUMMARY ---")
print("Final Balance:", balance)
print("Successful Transactions:", successful)
print("Rejected Transactions:", rejected)
