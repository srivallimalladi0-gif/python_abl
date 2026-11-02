1. Algorithm
Start.
Read the venue cost.
Read the equipment cost.
Read the catering cost.
Read the transport cost.
Read the certificate cost per participant.
Read the number of participants.
Read the registration fee per participant.
Read the sponsorship amount.
Calculate the total fixed cost.
Calculate the total certificate cost.
Calculate the total event cost.
Calculate the participant contribution.
Calculate the total available funds.
Calculate the sponsorship shortfall, if any.
Calculate the minimum registrations required to break even.
Display all results.
Stop.

PSEUDOCODE 
START

INPUT venue_cost
INPUT equipment_cost
INPUT catering_cost
INPUT transport_cost
INPUT certificate_cost
INPUT participants
INPUT registration_fee
INPUT sponsorship

fixed_cost = venue_cost + equipment_cost
             + catering_cost + transport_cost

total_certificate = certificate_cost * participants

total_cost = fixed_cost + total_certificate

participant_amount = participants * registration_fee

total_funds = participant_amount + sponsorship

IF total_funds >= total_cost
    shortfall = 0
ELSE
    shortfall = total_cost - total_funds
END IF

minimum_registrations =
    (fixed_cost - sponsorship) /
    (registration_fee - certificate_cost)

DISPLAY total_cost
DISPLAY participant_amount
DISPLAY shortfall
DISPLAY minimum_registrations

STOP

5. Computational Thinking
Decomposition: Divide the event budget into venue, equipment, catering, transport and certificate costs.
Pattern Recognition: Identify the common calculations of costs, contributions and funds.
Abstraction: Consider only the important financial details required for planning.
Algorithm Design: Develop step-by-step instructions to calculate expenses, funds and break-even registrations.
6. Important Formulas
Calculation Formula
Fixed cost Venue + Equipment + Catering + Transport
Total cost Fixed cost + Certificate cost
Participant contribution Participants × Registration fee
Total funds Participant contribution + Sponsorship
