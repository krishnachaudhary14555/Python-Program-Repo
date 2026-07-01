
# ------------Nested If & Multiple Conditions   ---------------#
# - When ,one Condition depends on another condition-------------3


print("Check your Elligibility")

age = int(input("Enter your age : "))

if(age >= 18):
    id_no = int(input("Enter your Id : "))
    if(id_no == 1234):
        print("🤞You can Enter")
    else:
        print("Wrong ID Number")
else:
    print("You Are Underage12")



# ---------------- Multiple Conditions (and) ------------#


age = int(input("Enter your age : "))
residence = input("Are you Indian ? : ")

if(age >= 18 and residence.lower() == "yes"):
    print("Eligible to drive")
else:
    print("Not Eligible to Drive")