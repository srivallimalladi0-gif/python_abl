Algorithm
Start.
Read the student email and registration ID.
Check whether the email contains @.
Check whether the email contains a valid domain and extension.
Check whether the email has invalid spaces or special characters.
Check whether the registration ID contains the required characters.
Verify the length and format of the registration ID.
Display whether the email and registration ID are valid or invalid.
Display the errors if any.
Stop.

PSEUDOCODE 
START

INPUT email
INPUT registration_id

IF email contains "@"
    IF email contains "." after "@"
        PRINT "Valid Email"
    ELSE
        PRINT "Invalid Email"
    ENDIF
ELSE
    PRINT "Invalid Email"
ENDIF

IF registration_id has correct length
    IF registration_id contains valid characters
        PRINT "Valid Registration ID"
    ELSE
        PRINT "Invalid Registration ID"
    ENDIF
ELSE
    PRINT "Invalid Registration ID"
ENDIF

STOP