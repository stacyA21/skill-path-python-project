"""In this file, you will find the exercises to complete.

If you cannot complete an exercise, and you need the result for following exercises, then we have included a commented
out import statement like this: `# from .solutions.exercise_1_1 import order_strings`. This was created with only a
very limited set of data and is no replacement for your own solution in order to successfully complete these exercises.
If you need help, please consult your mentor.

Note: these example solutions mention first names instead of full names. This is not representative of the actual expected
output.
"""

from datetime import date

from faker.typing import SeedType

import generate_data
from header_print import header_print

"""
We start you off with some random data to parse. Please replace the value of the `your_favourite_food` variable with
your own favourite food. This makes everyone's data unique.

PS: We assume that a customer is uniquely defined by their name. If "Martin Adams" appears multiple times in the data,
this is the same customer.
"""
print("⚙️ Generating data...")
your_favourite_food: SeedType = "I don't have a favourite dish"

customer_specs = generate_data.CustomerSpecs(num_customers=5_000, min_age=12, max_age=80)
order_specs = generate_data.OrderSpecs(num_orders_per_day=20, start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
data_string = generate_data.main(customer_specs=customer_specs, order_specs=order_specs, seed=your_favourite_food)

# Print first 100 characters of the data to see what it looks like, which is something like this:
# > Martin Adams ,51,M,Monday 01 January 2024,Bald,20;Victor Barnes,28,M,Monday 01 January 2024,Mohawk,40;...
print("🚀 Data generated correctly!")
print(f"Start of data_string: '{data_string[:100]}'")

"""
Exercise 1
==========
The data is now one big string, which makes it difficult to work with. You will have to parse it into a workable format.
This is what Exercise 1 is focused on. Follow the steps below.
"""
header_print("Exercise 1")

"""
Exercise 1.1
============
The data seems to have multiple orders, which are separated by a semicolon (;).

As the first step, create a list `orders_strings` where each entry is only the string corresponding to one order.
> Example output: ["Martin Adams ,51,M,Monday 01 January 2024,Bald,20", "Victor Barnes,28,M,Monday 01 January 2024,Mohawk,40", ...]
"""
header_print("Exercise 1.1")
orders_strings = []
for order in data_string.split(";"):
    orders_strings.append(order.strip())

orders_strings_new = '\n'.join(orders_strings)

print(orders_strings[:5])
"""
Exercise 1.2
============
Now that you have a list of order strings, it starts to look a bit more neat. However, how do you handle an individual
order and get insights from this?

As the next step in the data parsing, each element of the list should be a list itself. Make a new variable and name
it `orders_lists`.
> Example output: [["Martin Adams ", "51", "M", "Monday 01 January 2024", "Bald", "20"], ...]
"""
header_print("Exercise 1.2")
header_print("Exercise 1.2")
orders_lists = []

#split each string by ","
for order in orders_strings:
    orders_lists.append(order.split(","))


print(orders_lists[:5])


"""
Exercise 1.3
============
Great, each part of our list is now an individual order that we can use! The next issue pops up though: some names seem
to have some data corruption and they have some whitespaces before or after the name. See for example in our example
output above, that we have the name "Martin Adams " and not "Martin Adams" - this was not a typo ;)

As the next step, go through the list and remove the whitespaces from the start and end of names. Make a new variable
and name it `orders_cleaned`.
> Example output: [["Martin Adams", "51", "M", "Monday 01 January 2024", "Bald", "20"], ...]
"""
header_print("Exercise 1.3")
orders_cleaned = []
for order in orders_lists:
    order[0] = order[0].strip()
    orders_cleaned.append(order)
print(orders_cleaned[:5]) 

"""
Exercise 1.4
============
Awesome work! The names now seem to be cleaned and we are ready to go. Or are we? If you take a better look, there is
another issue. Can you spot it...?

Indeed, the integers in the list also seem to be strings. This means that we cannot perform numerical operations on
them, so we need to transform (aka cast) them.

As the next step, go through the orders and make the age of the customer and the price of the hairstyle integer. Make a
new variable and name it `orders_casted`.
> Example output: [["Martin Adams", 51, "M", "Monday 01 January 2024", "Bald", 20], ...]
"""
header_print("Exercise 1.4")
orders_casted = [
    [order[0], int(order[1]), order[2], order[3], order[4], int(order[5])]
    for order in orders_cleaned
]
print(orders_casted [:5]) 
"""
Exercise 2
==========
Congratulations! The data is now in a workable format and we can move on to the exciting part: extracting insights
from the data. Let's start with getting to know the data a little bit better.

For each sub-exercise, print it in the format: "Customer <name> got the haircut <hairstyle> on <date> for €<cost>.".
> Example output:
> "Customer Natalie Adams got the haircut Braided on Monday 30 December 2024 for €42.00."
> "Customer Caroline Barnes got the haircut Bald on Tuesday 31 December 2024 for €20.00."
> "Customer Glenn Collier got the haircut Pompadour on Tuesday 31 December 2024 for €38.00."
"""
header_print("Exercise 2")

"""
Exercise 2.1
============
What were the first 3 orders?
"""
header_print("Exercise 2.1")
orders_first_3 = ...
def print_order(order):
    name = order[0]
    hairstyle = order[4]
    date = order[3]
    cost = order[5]
    print(f"Customer {name} got the haircut {hairstyle} on {date} for €{cost}.")
for order in orders_casted[:3]:
    print_order(order)

"Customer {name} got the haircut {hairstyle} on {date} for €{cost}."
"""
Exercise 2.2
============
What were the last 5 orders?
"""
header_print("Exercise 2.2")
orders_last_5 = []
print("Last 5 orders:")
for order in orders_casted[-5:]:
    print_order(order)


 # Print the last 5 orders to verify the result

"""
Exercise 2.3
============
What was the 1000th order?
"""
header_print("Exercise 2.3")
order_1000 =[]
print("1000th order")
#iterate over the orders_casted list
for order in orders_casted[999:1000]:
    print_order(order)
"""
Exercise 2.4
============
What were the 2000th until 2025th orders?
"""
header_print("Exercise 2.4")
order_2000_to_2025 = []
print("2000 to 2025th order")
for order in orders_casted[1999:2025]:
    print_order(order)
"""
Exercise 3
==========
Of course, customers do not only get one haircut per year, so you expect to see some names in the data multiple times
(remember that we assume that the name of a customer is unique).

Find the unique customers that the hairdresser has served. Put the unique names in a variable called `unique_names`, and
then print how many there are in and who they are in this format: "There are ... unique names, namely ..."
> Example output: "There are 637 unique names, namely ['Terry Adams', 'Dennis Barnes', 'Beth Collier', ..."

Extra challenge: Try this with a set comprehension!
"""
header_print("Exercise 3")
unique_names = {order[0] for order in orders_casted}
print(f"There are {len(unique_names)} unique names, namely {list(unique_names)}.")

"""
Exercise 4
==========
The hairdresser would like to know how much revenue they made. Try to find the following and print the results:
"""
header_print("Exercise 4")

"""
Exercise 4.1
============
What was the total revenue in the data? Put this in a variable named `total_revenue`.
"""
header_print("Exercise 4.1")
total_revenue = 0
for order in orders_casted:
    total_revenue += order[5]
print(total_revenue)
"""
Exercise 4.2
============
What was the revenue in the month of March 2024? Put this in a variable named `revenue_march_2024`.
"""
header_print("Exercise 4.2")
revenue_march_2024 = 0
for order in orders_casted:
    if "March 2024" in order[3]:
        revenue_march_2024 += order[5]
print(revenue_march_2024)
"""
Exercise 4.3
============
What was the revenue on Mondays? What about on Sundays? Name these variables `revenue_mondays` and `revenue_sundays`.
"""
header_print("Exercise 4.3")
revenue_mondays = 0
revenue_sundays = 0
for order in orders_casted:
    if "Monday" in order[3]:
        revenue_mondays += order[5]
    elif "Sunday" in order[3]:
        revenue_sundays += order[5]
print(f"Revenue on Mondays: {revenue_mondays}")
print(f"Revenue on Sundays: {revenue_sundays}") 

"""
Exercise 4.4
============
The hairdresser would like to know the revenue per gender. They would also like to know how many orders were made per
gender, because they are interested in knowing the average order price per gender (rounded to 2 decimals).

You may assume that every customer's gender is one of M, F, or X.

For each gender, print in the following format:
> "Revenue <gender>: <revenue> (<count> clients). Average revenue: €<average_revenue>."
> Example output: Revenue M: €91,252.00 (2356 clients). Average revenue: €38.73.

Extra challenge: try to use only one for-loop to compute the necessary information for all genders.
"""
header_print("Exercise 4.4")
revenue_m = 0
revenue_f = 0
revenue_x = 0

for order in orders_casted:
    if order[2] == "M":
        revenue_m += order[5]
    elif order[2] == "F":
        revenue_f += order[5]
    elif order[2] == "X":
        revenue_x += order[5]

count_m = sum(1 for order in orders_casted if order[2] == "M")
count_f = sum(1 for order in orders_casted if order[2] == "F")
count_x = sum(1 for order in orders_casted if order[2] == "X")
average_revenue_m = round(revenue_m / count_m, 2)
average_revenue_f = round(revenue_f / count_f, 2)
average_revenue_x = round(revenue_x / count_x, 2)
print(f"Revenue M: €{revenue_m} ({count_m} clients). Average revenue: €{average_revenue_m}.")
print(f"Revenue F: €{revenue_f} ({count_f} clients). Average revenue: €{average_revenue_f}.")
print(f"Revenue X: €{revenue_x} ({count_x} clients). Average revenue: €{average_revenue_x}.")




"""
Exercise 4.5
============
Every year. the Institute of Statistics Netherlands (ISN) is doing research into the inflation trends in the
Netherlands. To do so, they collect data from as many hairdressers in the Netherlands as possible. Therefore, they have
reached out to you. They want to know the average price of a haircut.

Calculate the average price of a haircut and print the result in the following format:
> "Average price of a haircut: €<average_price_haircut>."

For this calculation, you can use the variable HAIRSTYLES, which is a list of tuples. The first element of each tuple is
the name of the haircut, the second element is the price. You can print it to inspect it.
"""
header_print("Exercise 4.5")
HAIRSTYLES = generate_data.HAIRSTYLES
print(f"{HAIRSTYLES=}")

average_price_haircut = 0
for hairstyle in HAIRSTYLES:
    average_price_haircut += hairstyle[1]
average_price_haircut /= len(HAIRSTYLES)
print(f"Average price of a haircut: €{average_price_haircut:.2f}.")


"""
Exercise 4.6
============
The ISN finally publishes its research results on the inflation trends in the Netherlands of the past year. In the last
chapter of the research report, the hairdresser reads that the average inflation is 3.5%. This means that, on average,
the cost of living has increased by 3.5%. To compensate for this, the hairdresser wants to increase the prices of
haircuts by 3.5%; however, only for the working class. This way, juniors (<18) and seniors (>65) will not be affected.
The hairdresser wants to know want the impact on the revenue would have been last year if they had raised their prices
by 3.5% last year already.

Apply the price change of 3.5% on the working class and calculate the new revenue. Name this new revenue variable
`total_revenue_inflation_correction`.

Print the result in the following format:
> "Revenue after price change: €<total_revenue_inflation_correction>."
"""
header_print("Exercise 4.6")
total_revenue_inflation_correction = 0

inflation = 3.5 / 100
for order in orders_casted:
    if order[1] > 18 or order[1] < 65:
        order[5] *= (1 + inflation)
        total_revenue_inflation_correction += order[5]
print(f"Revenue after price change: €{total_revenue_inflation_correction:.2f}.")
"""
Exercise 4.7
============
Well done! The hairdresser now wants to know difference in revenue if they actually had raised the prices of the
haircuts by 3.5% for the working class last year. Calculate the difference between the actual revenue (`total_revenue`)
and the predicted revenue after inflation correction (`total_revenue_inflation_correction`) and name this variable
`revenue_difference`.

Print the output in the following format:
> "Revenue increase after inflation correction: €<revenue_difference>."
"""
header_print("Exercise 4.7")

revenue_difference = total_revenue_inflation_correction - total_revenue
print(f"Revenue increase after inflation correction: €{revenue_difference:.2f}.")


"""
Exercise 4.8
============
The hairdresser is surprised! So much extra revenue. However, it just doesn't sit and feel right. The hairdresser wants
to know if they can afford to give some discount to juniors and seniors without losing the extra revenue due to the
price increase on the working class. The hairdresser decides to give a 10% discount to juniors and a 5% discount
to seniors (while still applying the 3.5% price increase on the working class).

Calculate the new revenue after this and call this revenue `total_revenue_discount`. Print the output in the following
format:
> "Revenue after discount: €<total_revenue_discount>."
"""
header_print("Exercise 4.8")
total_revenue_discount = 0
discount_juniors = 0.10
discount_seniors = 0.05
for order in orders_casted:
    if order[1] < 18:
        order[5] *= (1 - discount_juniors)
    elif order[1] > 65:
        order[5] *= (1 - discount_seniors)
    else:
        order[5] *= (1 + inflation)
    total_revenue_discount += order[5]
print(f"Revenue after discount: €{total_revenue_discount:.2f}.")


"""
Exercise 4.9
============
Calculate the difference in revenue again. However, this time, calculate the percentual increase and name the variable
`revenue_difference_percent`. Print the output in the following format:
> "Percentual revenue increase after discount: <revenue_difference_percent>%."
"""
header_print("Exercise 4.9")
# from .solutions.exercise_4_8 import total_revenue_discount
revenue_difference_percent = (
    (total_revenue_discount - total_revenue) / total_revenue * 100
)
print(f"Percentual revenue increase after discount: {revenue_difference_percent:.2f}%.")

"""
Exercise 4.10
============
Nice! The hairdresser will actually make <revenue_difference_percent>% more revenue the coming year with the planned
discounts for juniors and seniors, and the price increase for the working class. However, the hairdresser knows that the
Wavy haircut is very popular among juniors. Therefore, the hairdresser wishes to exclude this haircut from the discount
for juniors.

Calculate the new revenue after without the discount for the Wavy haircut for juniors and call this revenue
`total_revenue_discount_no_wavy`. Print the output in the following format:
> "Revenue after discount (no Wavy): €<total_revenue_discount_no_wavy>."
"""
header_print("Exercise 4.10")
total_revenue_discount_no_wavy = 0
for order in orders_casted:
    if order[1] < 18 and order[4] != "Wavy":
        order[5] *= (1 - discount_juniors)
    elif order[1] > 65:
        order[5] *= (1 - discount_seniors)
    else:
        order[5] *= (1 + inflation)
    total_revenue_discount_no_wavy += order[5]
print(f"Revenue after discount (no Wavy): €{total_revenue_discount_no_wavy:.2f}.")


"""
Exercise 5
==========
"""
header_print("Exercise 5")

"""
Exercise 5.1
============
The hairdresser is very happy with the data analysis so far and wishes to do this every year once the ISN research
results are out. To make this easier, the hairdresser would like to write a function that takes the list of orders as
input and returns the revenue. Write a function to do so. The function should be called `calculate_revenue` and takes
as input a list of orders and returns the total revenue.

Test the function on the original input, `orders_casted`, and see if you get the same revenue as calculated before
(`total_revenue`). Print the results in the following format:
> "Total revenue: <total_revenue>, Total revenue with function: <total_revenue_function>".
"""
header_print("Exercise 5.1")
total_revenue_function = ...
def calculate_revenue(orders):
    total_revenue = 0
    for order in orders:
        total_revenue += order[5]
    return total_revenue
total_revenue = calculate_revenue(orders_casted)
print(f"Total revenue: {total_revenue:.2f}, Total revenue with function: {total_revenue_function}")

"""
Exercise 5.2
============
So far, so good! Now the hairdresser wishes to include a scaling factor as input to the function. This scaling factor
will be applied to all orders. The scaling factor will reflect a price decrease/increase. For example, for a price
decrease of 5% we would input `scaling_factor=0.95` to the function, and for a price increase of 5% we would input
`scaling_factor=1.05`. Write this function!

Test the function on the original orders, `orders_casted`, with scaling factor for an increase of 7.5% and print the
result in the following format:
> "Revenue with scaling factor <scaling_factor> is <total_revenue_scaling_factor>".
"""
header_print("Exercise 5.2")
total_revenue_scaling_factor = ...
def calculate_revenue(orders, scaling_factor):
    total_revenue = 0
    for order in orders:
        total_revenue += order[5] * scaling_factor
    return total_revenue
scaling_factor = 1.075
total_revenue_scaling_factor = calculate_revenue(orders_casted, scaling_factor)
print(f"Revenue with scaling factor {scaling_factor} is {total_revenue_scaling_factor:.2f}.")

"""
Exercise 6
==========
The hairdresser wants to attract more customers in a fun way. The hairdresser decides to reward the first customer that
results in a total revenue passing the €1,000.00. Who was this customer in the original `orders_casted` list? When you
have found the lucky customer, print the following:
> "Reached revenue of €1,000.00. {name} is the lucky one! 🎉"

NB: You can assume the list `orders_casted` is sorted, meaning the first row is the first order, and the second row is
the second order, etc.
"""
header_print("Exercise 6")
winner = ...
def find_winner(orders):
    total_revenue = 0
    for order in orders:
        total_revenue += order[5]
        if total_revenue >= 1000:
            return order[0]
    return None
winner = find_winner(orders_casted)
print(f"Reached revenue of €1,000.00. {winner} is the lucky one! 🎉")
