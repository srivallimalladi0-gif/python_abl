Aim: To develop a Python program that calculates traffic violation fines based on vehicle category, offence type, repeat offences, and identifies driving disqualification conditions.
1. Algorithm
Start.
Read the number of violations.
Initialize total fine and disqualification count to zero.
Repeat for each violation:
Read vehicle category.
Read offence type.
Check whether it is a repeat offence.
Assign the fine based on the offence type.
If it is a repeat offence, increase the fine by 50%.
Calculate the final penalty.
Check disqualification conditions.
Display the fine for each violation.
Display total fine and disqualification status.
Stop.

 Pseudocode
START

Read number of violations

Set total_fine = 0
Set disqualification = 0

FOR each violation

    Read vehicle category
    Read offence type
    Read repeat status

    IF offence = "Helmet" THEN
        fine = 500

    ELSE IF offence = "Overspeeding" THEN
        fine = 1000

    ELSE IF offence = "No License" THEN
        fine = 5000

    ELSE
        fine = 0
        Display "Invalid Offence"
    END IF

    IF repeat status = "YES" THEN
        fine = fine * 1.5
    END IF

    IF offence = "No License" THEN
        disqualification = disqualification + 1
    END IF

    total_fine = total_fine + fine

    Display fine

END FOR

Display total fine

IF disqualification > 0 THEN
    Display "Disqualification Condition Identified"
ELSE
    Display "No Disqualification Condition"
END IF

STOP