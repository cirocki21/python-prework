# Question 1
def hello_name(user_name):
    print("Hello_" + user_name.upper() + "!")

hello_name('username')

#or

user_name = input("Type in your username: ")
hello_name(user_name)


# Question 2
def first_odd():
   for value in range (1,100,2):
       print(value)

first_odd()

# to return none 

print(first_odd())

# Question 3

def max_num_in_list(a_list):
    print(max(a_list))

number_list = list(range(1,101))

# This is if you want to put in your own range:

max_num_in_list(number_list)

first = int(input("Type in a number: "))
second = int(input("Type in a number higher than first number you typed in: ")) + 1

new_number_list = list(range(first,second))
 
print("\nHere is the max number of your numbers:")
max_num_in_list(new_number_list)

# Question 4

def is_leap_year(a_year):
    if year % 4 == 0: 
         print("This is a leap Year!")
    else:
          print("This is NOT a leap year")

year = int(input("Enter a year and I will tell you if it is a leap year: ")) 

is_leap_year(year)

# Question 5 

def is_consective(a_list):
    l = min(a_list)
    h = max(a_list) + 1
    if a_list == list(range(l, h)):
       print("This list IS consective!")
    else:
       print("This list is NOT consective!")
    
list_a =[1,2,4,5]
list_b = [1,2,3,4,5]
list_c = [1,2,3,4,5,6,8]

is_consective(list_c)










 


