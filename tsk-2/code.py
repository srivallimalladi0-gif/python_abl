# Case Study 2: 
        
import math

# Input details
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter number of participants: "))
fee = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate costs
fixed_cost = venue + equipment + catering + transport
certificate_total = certificate * participants
total_cost = fixed_cost + certificate_total

# Calculate funds
participant_amount = participants * fee
total_funds = participant_amount + sponsorship

# Calculate shortfall
shortfall = max(0, total_cost - total_funds)

# Calculate minimum registrations
if sponsorship >= fixed_cost:
    minimum = 0
elif fee > certificate:
    minimum = math.ceil(
        (fixed_cost - sponsorship) / (fee - certificate)
    )
else:
    minimum = -1

# Display results
print("\n--- CAMPUS EVENT REPORT ---")
print("Total Event Cost:", total_cost)
print("Participant Contribution:", participant_amount)
print("Total Funds:", total_funds)
print("Sponsorship Shortfall:", shortfall)

if minimum == -1:
    print("Break-even is not possible with this fee.")
else:
    print("Minimum Registrations:", minimum)

             
