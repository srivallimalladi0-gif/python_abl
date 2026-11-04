Case Study 5: Algorithm
Start.
Initialize the account balance.
Read the number of transactions.
Repeat for each transaction.
Read the transaction type (Deposit or Withdrawal).
If the transaction is a deposit:
Check whether the amount is positive.
Add the amount to the balance.
If the transaction is a withdrawal:
Check whether the amount is positive.
Check whether the amount is within the withdrawal limit.
Check whether sufficient balance is available.
Deduct the amount if all conditions are satisfied.
Otherwise, display an invalid transaction message.
Count successful and rejected transactions.
Display the final balance and transaction summary.
Stop.
2. PseudocodeSTART

Set balance = 5000
Set successful = 0
Set rejected = 0

Read number of transactions

FOR each transaction

    Read transaction type
    Read amount

    IF amount <= 0 THEN
        Display "Invalid Amount"
        rejected = rejected + 1

    ELSE IF transaction type = "D" THEN
        balance = balance + amount
        successful = successful + 1
        Display "Deposit Successful"

    ELSE IF transaction type = "W" THEN

        IF amount > 2000 THEN
            Display "Withdrawal Limit Exceeded"
            rejected = rejected + 1

        ELSE IF amount > balance THEN
            Display "Insufficient Balance"
            rejected = rejected + 1

        ELSE
            balance = balance - amount
            successful = successful + 1
            Display "Withdrawal Successful"
        END IF

    ELSE
        Display "Invalid Transaction Type"
        rejected = rejected + 1
    END IF

END FOR

Display final balance
Display successful transactions
Display rejected transactions

STOP
