cost_per_litre = 100
mileage_per_litre = 35
total_distance = int(input("Total Distance: "))
hotel_cost_per_day = 1000
hotel_stay_days =int(input("Total Stay days: "))
food_budget_per_day = int(input("Food budget per day : "))
total_eating_days = int(input("Number of eating days: "))
total_activity_budget = int(input("Activities budget: "))
total_trip_litres = int(total_distance) / int(mileage_per_litre)
total_fuel_cost = int(total_trip_litres)* int(cost_per_litre)
hotel_bill = int(hotel_cost_per_day) * int(hotel_stay_days)
food_bill = int(food_budget_per_day) * int(total_eating_days)
total_trip_cost =  total_fuel_cost + hotel_bill + food_bill + total_activity_budget
print(total_trip_cost)