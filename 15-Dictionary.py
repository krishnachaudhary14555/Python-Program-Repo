# ------ Dictionary ----------#

''' - A dictionary is like a real dictionary book : you search a word(key)  , you get a meaning (value)
     Unordered , mutable and indexed key-value pairs enclosed in {}
'''

student = {"name":"Rohit", "age":21, "city":"Pune"}
# print(student)


# # 2- Accessing values
# print(student["name"])  # Rohit
# print(student["age"]) 


# # 3- Adding and Updating
# student["Country"] = "India"   # adding
# student["age"]  = 34
# print(student)


# # 4- Removing 
# student.pop("age")
# print(student)


# # -5- Only keys  and values  -> Dictionary Methods
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))



# # - Looping
# for k in student:
#     print(k , ":" ,student[k])


# # - Nested dictionary 
# employee = {
#     "E101" : {"name":"Rohit","city":"Pune"},
#     "E102" : {"name":"Vijay","city":"Agra"}
# }
# print(employee)
# print(employee["E101"]["name"])

# - Mapper wrong -> correct
mapper ={
    "mombai":"Mumbai",
    "kolkatta":"Kolkata"
}
print(mapper["mombai"])