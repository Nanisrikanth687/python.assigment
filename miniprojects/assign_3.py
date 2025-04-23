# Write a Python program that calculates the electricity bill based on:
# • Units consumed (number)
# • User type: "residential" or "commercial"
# • Time of billing: "peak" or "off-peak"
# ⸻
# Conditions:
# 1. Residential Tariff (₹ per unit):
# • 0–100 units: ₹3
# • 101–300 units: ₹5
# • Above 300 units: ₹7
# 2. Commercial Tariff (₹ per unit):
# • 0–100 units: ₹6
# • 101–300 units: ₹8
# • Above 300 units: ₹10
# 3. Time-based Surcharge:
# • If time is "peak": Add 15% to the total bill.
# • If time is "off-peak": No extra charge.
# ⸻
# Input from User:
# • Enter units consumed
# • Enter user type (residential / commercial)
# • Enter time of billing (peak / off-peak)
# ⸻
# Output:
# • Show base price
# • Show any surcharge
# • Show final bill amount



print("####### ELECTRICITY BILL CALCULATOR #######")
total_bill = 0
rate_per_unit = 0
 
units = int(input("Enter units consumed: "))
user_type = input('Enter user type (residential / commercail): ')
billing_time = input("Enter time of billing  (peak/off-peak): ")
 
if user_type == "residential":
    if units > 0 and units <= 100:
        rate_per_unit = 3
    elif units > 100 and units <= 300:
        rate_per_unit = 5
    elif units > 300:
        rate_per_unit = 7
else:
    if units > 0 and units <= 100:
        rate_per_unit = 6
    elif units > 100 and units <= 300:
        rate_per_unit = 8
    elif units > 300:
        rate_per_unit = 10
 
 
base_bill = units * rate_per_unit
 
if billing_time == "peak":
    total_bill = base_bill + 5
else:
    total_bill = base_bill
 
 
print(f'''
   ####### YOUR TOTAL BILL #######
   Your Connection Type: {user_type}
   Total Units Consumed: {units}
   Your Rate Per Unit: {rate_per_unit}
   Total Base Price: {base_bill}
   -----------------------------------
   Total Bill: {total_bill}
   -----------------------------------
''')