import sqlite3 #imports sqlite3 library
import time
import hashlib

import queries

logged_in = False
admin = False
current_UUID = 0

#connecting to the database
db = sqlite3.connect("L4HDPGF2-E1.db")
db.row_factory = sqlite3.Row
query = db.cursor()

def admin_panel(admin):
    
    sql = f"""
        SELECT administrator
        FROM accounts
        WHERE UUID = '{current_UUID}';
    """
    
    for row in query.execute(sql):
        admin = row["administrator"]
    
    if admin == 0:
        admin = False
    elif admin == 1:
        admin = True
        
    if admin == True:
        action = input("\n(Administrator) What would you like to do, (Type !help for options): ")
        match action:
            case "!help":
                print("get-admin, update-admin, ubisoft (removes inactive players)")
            case "get-admin":
                queries.get_admin()
            case "update-admin":
                queries.modify_admin()
            case "ubisoft":
                queries.ubisoft()
            case _:
                print("\nThat wasn't on the list idiot!")
            
    else:
        print("\nYou do not have permission to access this section of the program. Do you really care about being an admin that much, jeez go outside and touch some grass.")

while logged_in == False:
    #get user input
    action = input("\nWhat would you like to do, (Type !help for options): ")
    
    match action:
        case "!help":
            print("\nOptions: sign-up, log-in")
        case "sign-up":
            queries.sign_up()
            logged_in = True
            current_UUID = queries.get_user()
        case "log-in":
            admin = queries.log_in()
            logged_in = True
            current_UUID = queries.get_user()
        case _:
            print("\nThat wasn't on the list idiot!")

while logged_in == True:
    #get user input
    action = input("\n(Non Administrator) What would you like to do, (Type !help for options): ")
    
    match action:
        case "!help":
            print("\nOptions: log-out, admin-panel, change-class")
        case "log-out":
            logged_in = False
            admin = False
        case "admin-panel":
            admin_panel(admin)
        case "change-class":
            queries.change_class()
        case "get-class":
            queries.get_class()
        case _:
            print("\nThat wasn't on the list idiot!")