1.start
2.Read the number of students 
3.Enter each student's name, aggregate marks, subject marks, attendance, and family income.
4.Check whether aggregate marks are at least 75%.
5.Check whether every subject mark is at least 60%.
6.Check whether attendance is at least 75%.
7.Check whether family income is below ₹2,50,000.
8.If all conditions are satisfied, select the student as eligible.
9.Store eligible students in a list.
10.Sort students based on aggregate marks in descending order.
11.If marks are equal, give priority to higher attendance.
12.If attendance is also equal, give priority to lower family income.
13.Display the final scholarship ranking.
14.Stop.

PSEUDOCODE

START

INPUT number of students

CREATE empty eligible list

FOR each student

    INPUT name
    INPUT aggregate marks
    INPUT subject marks
    INPUT attendance
    INPUT family income

    IF aggregate marks >= 75 AND
       all subject marks >= 60 AND
       attendance >= 75 AND
       family income <= 250000 THEN

          ADD student to eligible list

    ELSE
          DISPLAY "Not Eligible"
    END IF

END FOR

SORT eligible students BY
    aggregate marks DESCENDING
    attendance DESCENDING
    family income ASCENDING

DISPLAY scholarship ranking

STOP

 Conclusion
This program checks student eligibility using marks, attendance, and family income. It selects eligible students and ranks them based on aggregate marks, attendance, and income. It helps universities allocate scholarships fairly.
Note: The eligibility limits and tie-breaking rules used here are sample rules for this assignment. Actual university scholarship rules may differ.