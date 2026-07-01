# Input & Type Casting 


 #Input  , evertihing you type using input beacomes a string , even numbers
# name = input("Enter your name : ")
# print("Welcome ", name )


''' Type casting -->
     changing the type of the data  into another using built-in Python functions int(), float(), str()
     '''

# age = int(input("Enter your age : "))
# print(type(age))
# print("Age :", age)

# temp =36.45
# print(type(temp)) # float type

# print(type(str(temp)))  #string type



''' Common Mistakes 
 1- forgetting to convert input ->num
 2- adding str + num -> error
 3- using int() on decimal values 
 4- Not spacing messeges 
 '''


emp_name = input("Enter employee name : ")
basic_sal = float(input("Basic Salary : "))
bonus = float(input("Bonus Amount : "))
tax = float(input("Enter tax percentage :  "))
 
print("--------------Salary Slip -----------------")
gross_sal =basic_sal + bonus
print("Gross Salary : ", gross_sal)

tax_amount = gross_sal * tax/100.0
print("Tax Amount : ",tax_amount)

Net_sal = gross_sal - tax_amount
print("Net Salary : ",Net_sal)
