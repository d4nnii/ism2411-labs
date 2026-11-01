# AI Disclosure: AI was used to explain the errors and help me understand what needed to be fixed for exercise 5.

# Self Assesment Questions:
#1: The first bug I noticed was the total not adding the sales together. I noticed it by looking at the code and thinking though what each line was doing but the AI helped me understand it better. This shows that I'm starting to get better at finding simple logic errors but may need to work on it more.
#2: apply_disount(price, tier) takes a price and a discount tier as inputs and uses them to calculate the discounted price. It then returns the new price after the discount is applied. A colleague could probably use it without reading the code becuase the the name and inputs explains what it does.
#3: AI helped me better build my understanding because I still had to look at the code and understand what was wrong, it basically explained the errors in simple words for me instead of giving me the answers.

# Exercise 1:

# Define calculate tax function
def calculate_tax(price,rate):
    return price * rate

# Calling the function
tax1 = calculate_tax(100,0.07)
tax2 = calculate_tax(250,0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") #7.00
print(f"Tax on $100 at 8%: ${tax2:.2f}") #20.00
# Alternative for not defining apart: print (f"Another Tax: ${calculate_tax}(150,0.05):.2f")  -> 7.50

# Exercise 2:

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function
price = 200
tiers = ["gold", "silver", "bronze", "none"]  

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3:

# Write it out manually first, then refactor into a function
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function
def final_price(price, tier, tax_rate):
    disounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return disounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4:

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5:

# Fix Explanation: I fixed the total so it adds each sale instead of replacing the previous value. I also added the missing colon to the for loop and changed the while condition so it stops before trying to access an index that doesn't exist.

#broken_sales.py fixed:
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Exercise 6:

x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?