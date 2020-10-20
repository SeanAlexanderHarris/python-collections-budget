from . import Expense
import collections
import matplotlib.pyplot as plt

# Read the expenses csv file

expenses = Expense.Expenses()

expenses.read_expenses('data/spending_data.csv')

# loop through the list of expenses read from the csv & append to category list

spending_categories = []

for expense in expenses.list:
    print(expense.vendor)
    spending_categories.append(expense.category)

# initialize a spending counting object & grab the top 5 categories (dictionary)
spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)

# separate the keys & values of the top5 dictionary
categories, count = zip(*top5)

# use keys & values to construct bar chart, label it, show it
fig, ax = plt.subplots()

ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()
