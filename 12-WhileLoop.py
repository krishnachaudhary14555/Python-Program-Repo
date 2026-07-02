# ------------While Loop --------------------------#
# Repeat a task as long as a condition is true-------------


# # 1- Basic  While Loop
# i = 1 
# while  i<= 5:
#     print(i)
#     i+=1


# # 2-  Count Down 
# n = 5
# while n >= 1:
#     print(n)
#     n-=1


# # 3- Ask user until valid input
num =""
while not num.isnumeric():
    num = input("Enter any value: ")
    print("Please enter only number")
print("Number accepted : ",num)


# # Loop through list using while loop
# items = ["Apple","Banana","Mango","Papaya"]
# i=0
# while i < len(items):
#     print(items[i])
#     i+=1


# # 5- Using break 
# x=1
# while x <= 10:
#     if x == 5:
#         break
#     print(x)
#     x +=1




# # 6- Using Continue
# y=0
# while y <= 10:
#     if y % 2 ==0:
#         y+=1
#         continue
#     print(y)
#     y+=1


# 7- Password System 
password = ""
attempts = 3
while password != "Admin123" and attempts > 0:
    password = input("Enter valid Password : ")
    attempts -= 1
    if password == "Admin123":
        print("You can access")
    else:
        print("Sorry! You can not Access. Wrong Password")
print(attempts," attempts left ,Please try after sometime.")