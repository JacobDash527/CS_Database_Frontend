import sqlite3 #imports sqlite3 library
import time
import hashlib

import query

logged_in = False
admin = False

while logged_in == False:
    #get user input
    action = input("\nWhat would you like to do, (Type !help for !options): ")
    
    match action:
        case "!options":
            query.print("\nOptions: sign-up, log-in")
        case "sign-up":
            query.sign_up()
        case "log-in":
            admin = query.log_in()

while logged_in == True:
    #get user input
    action = input("\nWhat would you like to do, (Type !help for !options): ")
    
    match action:
        case "!options":
            print("\nOptions: log-out, admin-panel")
        case "log-out":
            logged_in = False
            admin = False
        case "admin-panel":
            query.admin_panel(admin)

def admin_panel(admin):
    if admin == True:
        action = input("\nWhat would you like to do, (Type !help for !options): ")
        match action:
            case "!options":
                print("modify-admin")
            case "modify-admin":
                query.modify_admin()
    else:
        print("You do not have permission to access this section of the program. Do you really care about being an admin that much, jeez go outside and touch some grass.")