Aim: To develop a Python program that calculates railway fares for multiple passengers based on distance, travel class, age concessions, reservation fees, and cancellation penalties.
1. Algorithm
Start.
Read the number of passengers.
Initialize the total fare to zero.
For each passenger:
Read passenger name, age, distance and travel class.
Calculate basic fare based on distance.
Calculate fare according to travel class.
Apply age-based concession if eligible.
Add reservation fee.
Calculate cancellation penalty if the ticket is cancelled.
Calculate the final fare.
Display the fare for each passenger.
Display the total amount.
Stop.

START

Read number of passengers
Set total = 0

FOR each passenger

    Read name
    Read age
    Read distance
    Read travel class

    IF distance <= 100 THEN
        fare = distance * 1
    ELSE IF distance <= 500 THEN
        fare = distance * 1.5
    ELSE
        fare = distance * 2
    END IF

    IF class = "AC" THEN
        fare = fare * 2
    ELSE IF class = "SL" THEN
        fare = fare * 1
    END IF

    IF age >= 60 THEN
        fare = fare * 0.8
    END IF

    reservation = 50
    fare = fare + reservation

    Read cancellation status

    IF cancellation = "YES" THEN
        penalty = fare * 0.25
        fare = fare - penalty
    END IF

    Display passenger fare
    total = total + fare

END FOR

Display total fare

STOP