import sqlite3 #imports sqlite3 library

db = sqlite3.connect("L4HDPGF2-E1.db")
db.row_factory = sqlite3.Row
query = db.cursor()

# sql = f"""
#         SELECT UUID
#         FROM accounts
#         WHERE email_address = "jacobdash527@gmail.com";
#         """

# for row in query.execute(sql):
#     print(row)
#     print(f"{row['UUID']}")

# sql = f"""
#     DELETE FROM accounts
#     WHERE days_since_login >= 365;
#     """
    
# query.execute(sql)
# db.commit()
    
# print("\nAhh yes I love taking away peoples rights!")

# class_name = ""
    
# sql = f"""
#     SELECT classes.class_name
#     FROM profiles, classes
#     WHERE UUID = "4"
#     AND profiles.class_ID = classes.class_ID;
#     """
# 7
# for row in query.execute(sql):
#     class_name = row['class_name']

# print(f"\nYour current selected class is {class_name}")

# username = input("\nEnter the users username: ")

# sql = f"""
#     SELECT accounts.administrator
#     FROM accounts, profiles
#     WHERE profiles.username = "{username}"
#     AND accounts.UUID = profiles.UUID;
#     """
    
# for row in query.execute(sql):
#     if row['administrator'] == 1:
#         print(f"{username} is an administrator.")
#     else:
#         print(f"{username} is not an adminstrator.")

# add_or_remove = int(input("Enter 1 for add and 0 for remove to return press enter: "))
    
# if add_or_remove != 1 and add_or_remove != 0:
#     print("\nThat is not an option!")
#     pass

# username = input("Input the users username: ")

# sql = f"""
#     UPDATE accounts
#     SET administrator = {add_or_remove}
#     FROM profiles
#     WHERE profiles.username = "{username}"
#     AND accounts.UUID = profiles.UUID;
#     """

# query.execute(sql)
# db.commit()

# #I am going insane this is starting to look like valve dev comments
# print("\nBye bye administrator!!!")

# current_UUID = 4

# sql = f"""
#     SELECT administrator
#     FROM accounts
#     WHERE UUID = "{current_UUID}";
#     """
    
# print(current_UUID)

# for row in query.execute(sql):
#     admin = row["administrator"]
#     print(row["administrator"])