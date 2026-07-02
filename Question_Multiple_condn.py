'''
Condition 1:
Ask the user to enter a security code.
If the security code is correct (5566) → move to Condition 2
If the code is wrong → print "Invalid security code." and stop.
Condition 2:
Ask the user to enter their employee department.
If the department is "Finance" → move to Condition 3
If not Finance → print "Access denied: Department not allowed." and stop.
Condition 3:
Ask the user for their access level.
If the access level is 5 or above → print "Access Granted: Welcome to the meeting room."
If access level is less than 5 → print "Insufficient access level."
'''

# security_code = int(input("Enter youe Security Code : "))

# if(security_code == 5566):
#     Emp_dept = input("Enter your Department : ")
#     if(Emp_dept.title() == "Finance"):
#         level = int(input("Enter your access Level : "))
#         if(level >= 5):
#             print("Welcome to the meeting room.")
#         else:
#             print("Insuficient access level.")
#     else:
#         print("Access Denied : Department not allowed.")
# else:
#     print("Inavlid Security COde .")





'''
2-- • Create a program for an online exam system:
• Ask the user for a registration number.
• If reg no = 1221, go ahead
• Else: “Registration failed.”
• Ask for exam subject.
• If subject is Python, continue
• Else: “Subject not available.”
• Ask for password.
• If password = 8888, print “Login successful! Start your exam.”
• Else: “Wrong password.”
'''

Reg_no = int(input("Enter your Registration number : "))
if(Reg_no == 1221):
    Exam_sub = input("Enter you Subject : ")
    if(Exam_sub.title() == "Python"):
        password = int(input("Enter your Password : "))
        if(password == 8888):
            print("Login Successful! Start your Exam ✅")
        else:
            print("Wrong Password")
    else:
        print("Subject not Available")
else:
    print("Registration failed ❌.")