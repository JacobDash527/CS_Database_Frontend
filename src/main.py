import sqlite3 #imports sqlite3 library
import time
import hashlib

import query

logged_in = False
admin = False
current_UUID = 0

while logged_in == False:
    #get user input
    action = input("\nWhat would you like to do, (Type !help for options): ")
    
    match action:
        case "!help":
            query.print("\nOptions: sign-up, log-in")
        case "sign-up":
            query.sign_up()
            logged_in = True
            current_UUID = query.get_user()
        case "log-in":
            admin = query.log_in()
            logged_in = True
            current_UUID = query.get_user()

while logged_in == True:
    #get user input
    action = input("\nWhat would you like to do, (Type !help for options): ")
    
    match action:
        case "!help":
            print("\nOptions: log-out, admin-panel, change-class")
        case "log-out":
            logged_in = False
            admin = False
        case "admin-panel":
            query.admin_panel(admin)
        case "change-class":
            query.change_class()

def admin_panel(admin):
    if admin == True:
        action = input("\nWhat would you like to do, (Type !help for options): ")
        match action:
            case "!help":
                print("modify-admin")
            case "modify-admin":
                query.modify_admin()
    else:
        print("You do not have permission to access this section of the program. Do you really care about being an admin that much, jeez go outside and touch some grass.")