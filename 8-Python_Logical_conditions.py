# --------------IF-ELSE -------------
# FITER DATA, VALIDATE INPUTS , CATEGORIZE VALUES

age = int(input("Enter your age : "))
if(age>=18):
    print("Adult")
else:
    print("Not Adult")




# # ------------Discount Checker -------------------#
# amount= int(input("Enter Amount : "))
# if(amount >= 1000):
#     print("You get a Discount")
# else:
#     print("No Discount")




# #----------- if-elif-else (Multiple Conditions)-----------#
# marks = int(input("Enter your marks :"))
# if(marks >= 90):
#     print("Grade A")
# elif(marks >= 60 ):
#     print("Grade B")
# elif(marks >= 35 ):
#     print("Grade C")
# else:
#     print("Fail")









# # ---------------- String Comparision Example --------------#
# city="Delhi"
# if( city.lower() == "delhi"):
#     print("City Matched")
# else:
#     print("Not Matched")




# # ------------Email Validation --------------#
# email = input("Enter your Email : ")
# if("@" in email and "." in email ):
#     print("Valid Email")
# else:
#     print("Invaild Email")








# --------------- Advanced : Missing Data Check----------#
value = input("Enter Data : ")
if(value == ""):
    print("Missing Data Found")
else:
    print("Data Available")