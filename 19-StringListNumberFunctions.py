 # ------ String , List & Number Functions -------------#
''' Built-in Functions aree like shortcuts in Python, gives us ready-made tools
Tech-define -> Built -in functions are pre-defined functions in Python that helps perform operations quickly and efficiently on Strings , Lists  and Numbers'''


# # A - STRING FUNCTIONS
# text = "Banana"
# print(text.count("a"))

# print("Hello.py".endswith(".py"))  # True

# print("Sales_Report.csv".startswith("Sales"))

# print("123".isnumeric())
# print("HI".isalpha())
# print("12HI".isalnum())

# print("Line1\nLine2\nLine3".splitlines())   #['Line1', 'Line2', 'Line3']


# # B- List Functions
# nums= [5,3,4,7,8,1]
# nums.sort()
# print(nums)


# fruits = ["banana","apple","mango"]
# fruits.sort()
# print(fruits)
# print(sorted(fruits))


# marks= [10,34,70]
# print(f"Max : {max(marks)} , Min : {min(marks)} , Sum : {sum(marks)}")


# my_list = [1,2,3,1,3,4]
# print(my_list.count(3)) # it counts fre of 3
# print(my_list[3])  # it return val of 3rd index  is 1
# print(my_list.index(3))  # it returns index of  3 is 2


# a = [1,2]
# b = [3,4]
# a.extend(b)
# print(a)  # [1, 2, 3, 4]



# # C- Number FUNCTIONS
# print(round(3.678,2))   # 3.68
# print(abs(-50))  # 50
# print(pow(5, 2))  # 25
# print(divmod(10,3))  # (3, 1)
# print(divmod(9,3))  # (3, 0)
# print(sum([10,5],5)) # 20

# # Practical use 
# products = [" mobile" , "Laptop", "TABLE"]
# clean = [p.strip().title() for p in products]
# clean.sort()
# print(clean)  # ['Laptop', 'Mobile', 'Table']


# # Find Out domain
# emails = ["rohit@gmail.com", "sneha@yahoo.com"]
# domains = [mail[mail.find("@")+1 : ] for mail in emails]
# print(domains)   # ['gmail.com', 'yahoo.com']



#  Check Valid Mobile No
mobiles = ["4578963214" ,"5678986532","4512784512"]
valid = [m  for m in mobiles if m.isdigit() and len(m) == 10]
print(valid)

