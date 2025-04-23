
basic_plan_name = "Basic"
basic_plan_cost = 29.99
basic_plan_includes_pool = False
basic_plan_includes_classes = False
basic_plan_guest_passes = 0
standard_plan_name = "Standard" 
standard_plan_cost = 49.99
standard_plan_includes_pool = True
standard_plan_includes_classes = False
standard_plan_guest_passes = 1
premium_plan_name = "Premium"
premium_plan_cost = 79.99
premium_plan_includes_pool = True
premium_plan_includes_classes = True
premium_plan_guest_passes = 3
# User information
customer_name = input("Enter your name: ")
customer_age = int(input("Enter your age: "))
customer_weight_kg = float(input("Enter your weight in kg: "))
customer_height_cm = float(input("Enter your height in cm: "))

expected_visits = int(input("How many times do you plan to visit the gym per month? "))
wants_pool = input("Do you want to use the pool? (yes/no): ").lower() == "yes"
wants_classes = input("Do you want to attend fitness classes? (yes/no): ").lower() == "yes"
needs_guest_passes = int(input("How many guest passes will you need per month? "))

cost_per_visit_per_basic_plan = basic_plan_cost * expected_visits 
cost_per_visit_per_standard_plan = standard_plan_cost  * expected_visits 
cost_per_visit_per_premium_plan = premium_plan_cost  * expected_visits

print("---plans per each visit----")

print(f"cost_per_visit_per_basic_plan. {expected_visits} * {basic_plan_cost } = Rs.{cost_per_visit_per_basic_plan}") 
print(f"cost_per_visit_per_standard_plan. {expected_visits} * {standard_plan_cost } = Rs.{cost_per_visit_per_standard_plan}") 
print(f"cost_per_visit_per_premium_plan. {expected_visits} * {premium_plan_cost } = Rs.{cost_per_visit_per_premium_plan}")

print("------Body Mass index-----")
body_mass_index =  customer_weight_kg / (customer_height_cm /100)**2
print(body_mass_index)

print("------basal metabolic rate---------")
body_BMR = (10*customer_weight_kg) +(6.25* customer_height_cm)-(5*customer_age) + 5
print(body_BMR)


print("-------Compare plans based on features needed and cost per visit---------")
print("********Basic_plan_features********")
Basic_plan_features = {
    "Basic":    {"cost": basic_plan_name, "pool": False, "classes": False, "guests": 0}
}
print(Basic_plan_features)

print("********standard_plan_features********")
standard_plan_features = {
    "Standard": {"cost": standard_plan_name, "pool": True,  "classes": False, "guests": 1}
}
print(standard_plan_features)

print("********premium_plan_features********")
premium_plan_features = {
    "Premium":  {"cost": premium_plan_name, "pool": True,  "classes": True,  "guests": 3}
}
print(premium_plan_features)
