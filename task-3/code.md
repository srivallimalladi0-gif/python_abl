1. Algorithm
Start.
Read the number of applicants.
Read each applicant's name.
Read subject marks and aggregate marks.
Check subject eligibility.
Check the minimum aggregate marks.
Check the course-specific cut-off marks.
If all conditions are satisfied, add the applicant to the eligible list.
Sort eligible applicants based on aggregate marks in descending order.
If aggregate marks are equal, compare subject marks.
If subject marks are also equal, compare entrance exam marks.
Assign ranks to eligible applicants.
Display the ranked list.
Stop.

PSEUDOCODE 
START

INPUT number_of_applicants

FOR each applicant

    INPUT name
    INPUT subject_marks
    INPUT aggregate_marks
    INPUT entrance_marks

    IF subject_marks >= subject_cutoff AND
       aggregate_marks >= minimum_marks

        ADD applicant to eligible list

    END IF

END FOR

SORT eligible list by:
    1. Aggregate marks (descending)
    2. Subject marks (descending)
    3. Entrance marks (descending)

DISPLAY ranked eligible applicants

STOP
