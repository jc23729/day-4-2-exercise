import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Get the total num of items in a list
num_items = len(names)
#we did import random up top
#Generate random numbers between 0 and the last index and turned it into a variable with random_choice
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay_bill= names[random_choice]

print(person_who_will_pay_bill + " is going to buy the meal today!")