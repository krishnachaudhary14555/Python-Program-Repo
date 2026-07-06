# ----------------------Functions ----------------------#
'''# - You give Input, Machine processes it and Gives Output-#
# Defined uding def keyword -> Syntax : def function_name():# code

function( def , return)
'''

# # 1- function no arguments
# def greet():
#     print("Hello world!")
# greet()

# # 2- function With Arguments 
# def welcome(name):
#     print("Welcome",name)

# welcome("Krishna")


# def  add(a,b):
#     print("a + b = ",a+b)
#     print("a * b = ",a*b)
# add(3,4)


# # - 3- With Return type
# def  add(a,b):
#     return a+b
# result = add(5,5)        # return helps us to reuse this value in any function
# print("a + b = ",result)
# def Multiply(x):
#     return x * 2
# mul = Multiply(result)
# print(mul)




# # 4- Clean Text 
# def clean_text(value):
#     return value.strip().title()
# res= clean_text("        krisHna chauDhary")
# print("Res : ",res)





# # 5- Fix City
# def fix_city(city):
#     city = city.lower().strip()
#     city = city.replace("mombai","Mumbai")
#     return city
# print(fix_city("        mombai"))



# #  6- - Get last digits
# def get_year(code):
#     return code[-4: ]
  
# digit = get_year("Laptop-2034")
# print(digit)





# # - 7 .Check valid Email
# def valid_email(email):
#     return '@' in email and '.' in email
# mail = valid_email("student@example.com")
# print("Email : ",mail)   # True



# # 8- Total salary
# def totla_salary(basic, bonus):
#     return basic + bonus
# total = totla_salary(60000, 5000)
# print("Total Salary : ",total)


# # 9- find numbers 
# def stats(nums):
#     return min(nums),max(nums),sum(nums)/len(nums)
# res = stats([12,30,50,10])
# print(res)



# 10- Clean List
def Clean_list(values):
    cleaned=[]
    for v in values:
        cleaned.append(v.strip().title())
    return cleaned
Cleaned_list = Clean_list([" delhi", "MuMBAi", "    AGRA"])
print("Cleand : ",Cleaned_list)
    

