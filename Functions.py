problem #1

day = input("Enter the day category(weekday,weekend): ").lower()
age = input("Enter your age category(adult,child,senior): ")
fam_input = input("Are you with family?: ").lower()
ticket = 0
adult_discount = 50
child_discount = 20
senior_discount = 30
family_discount = 10

def calculate_ticket_price():
    global ticket
    if age == "adult":
        if day == "weekday":
            ticket = 600
        elif day == "weekend":
            ticket = 500
    elif age == "child":
        if day == "weekday":
            ticket = 200
        elif day == "weekend":
            ticket = 100
    elif age == "senior":
        if day == "weekday":
            ticket = 400
        elif day == "weekend":
            ticket = 300
    else:
        print("Invalid age")
        return calculate_ticket_price()

def calculate_discount():
    global ticket
    if age == "adult":
        ticket -= adult_discount
    elif age == "child":
        ticket -= child_discount
    elif age == "senior":
        ticket -= senior_discount

def apply_family_discount():
    global ticket
    if fam_input in [ "yes"]:
        ticket -= family_discount
    elif fam_input in ["no"]:
        pass  

calculate_ticket_price()
calculate_discount()
apply_family_discount()

print(f"Your ticket price is {ticket}")

Problem #2

def calculate_rest_bill():
    items = input("Enter the ordered items : ").split(",")
    
    quantities = input("Enter the quantities of each item : ").split(",")
   
    prices = input("Enter the prices of each item : ").split(",")
  
    num_friends = int(input("Enter the number of friends to split the bill with: "))

    total_amount = 0
    for i in range(len(items)):
        item_total = int(quantities[i]) * float(prices[i])
        total_amount += item_total

  
    if num_friends > 0:
        total_amount /= num_friends

    return total_amount


total_bill = calculate_rest_bill()
print("The total bill amount per friend is", total_bill)

Problem #4

def estimate_travel_cost(destination, travel_style='budget', duration=7):
    base_costs = {
        'budget': {'transportation': 300, 'accommodation': 50, 'activities': 30},
        'luxury': {'transportation': 800, 'accommodation': 200, 'activities': 100}
    }
    if travel_style not in base_costs:
        raise ValueError("Invalid travel style. Choose 'budget' or 'luxury'.")
    costs = base_costs[travel_style]
    total_cost = sum(cost * duration for cost in costs.values())
    return total_cost
destination = input("Enter the destination: ")
travel_style = input("Enter the travel style (budget/luxury): ")
duration = int(input("Enter the duration of the trip (in days): "))
total_travel_cost = estimate_travel_cost(destination, travel_style, duration)
print(f'Estimated travel cost for {duration} days in {destination} ({travel_style}): ${total_travel_cost}')
