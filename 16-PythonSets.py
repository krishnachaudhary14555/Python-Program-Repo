# ------------ Sets --------------------------- #
# - A set is an Unordered , mutable collection that stores unique value only  / - Created using { { } ---#


# - 1- Create Sets 
fruits = {"Apple","Banana","Apple","Mango"}
print(len(fruits)) # 3
print(fruits)


# # 2- Add item 
# fruits.add("Orange")
# print(fruits)


# # 3- Remove Item
# fruits.discard("Mango")
# print(fruits)


# # 4- Set Operations 
# a= {1, 2, 3}
# b = {3 ,4 ,5}
# print("Union : ",a | b)     #Union :  {1, 2, 3, 4, 5}
# print("Intersection : ",a & b)      #  {3}
# print("Difference : ", a - b)       # {1, 2}
# print("Difference (b-a) : ", b - a)       # {4, 5}
# print("Symmetric Difference : ",a ^ b)  #  {1, 2, 4, 5}



# # 5- Remove Duplicates 
# cities = ["Mumbai","Pune","Delhi","Mumbai"]
# unique = set(cities)
# print("Unique values : ",unique)



# # - 6- Missing Values
# set1 = {"SQL","Excel","Power BI"}
# set2 = {"SQL","Power BI"}
# missing = set1 - set2
# print("MIssing : ", missing)  #{'Excel'}



# 7- Common Skills 
dept1= {"SQL","Python","Excel"}
dept2 = {"Excel","Python","Power BI"}
print("Common Skills : ",dept1 & dept2)  # O/P ->  {'Python', 'Excel'}