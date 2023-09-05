import sqlite3 #imports sqlite3 library
import time
import hashlib

logged_in = False
admin = False

#connecting to the database
db = sqlite3.connect("test.db")
db.row_factory = sqlite3.Row
query = db.cursor()

print("Database connected.")

def sign_up():
    email_addr = input("\nEmail address: ")
    password = input("\nPassword: ")

    passwd_hash = hash(password)

    sql = f"""

            INSERT INTO accounts(email_address, password_hash)
            VALUES("{email_addr}", "{passwd_hash}");
            """

    query.execute(sql)
    db.commit()

def log_in():
    email_addr = input("\nEmail address: ")
    password = input("\nPassword: ")

    passwd_hash = hash(password)

    sql = f"""
            SELECT password_hash, administrator
            FROM accounts
            WHERE email_address = "{email_addr}";
            """
    
    for row in query.execute(sql):
        resulst = [row['password_hash'], row['administrator']]
    
    if passwd_hash == resulst[0]:
        print("\nLogin successful!")
    
    if resulst[1] == 1:
        admin = True

#hash the inputted message
def hash(message_in):
    m = hashlib.new("sha256")
    m.update(message_in.encode())
    return(m.hexdigest())

def modify_admin():
    add_or_remove = input("Enter 1 for add and 0 for remove: ")
    user_email_addr = input("Input the users email address: ")

    sql = f"""

            INSERT INTO accounts(administrator)
            VALUES("{add_or_remove}")
            WHERE email_address = {user_email_addr};
            """

    query.execute(sql)
    db.commit()

def admin_panel():
    if admin == True:
        action = input("\nWhat would you like to do, (Type !help for !options): ")
        match action:
            case "!options":
                print("modify-admin")
            case "modify-admin":
                modify_admin()
    else:
        print("You do not have permission to access this section of the program. Do you really care about being an admin that much, jeez go outside and touch some grass.")


while logged_in == False:
    #get user input
    action = input("\nWhat would you like to do, (Type !help for !options): ")
    
    match action:
        case "!options":
            print("\nOptions: sign-up, log-in")
        case "sign-up":
            sign_up()
        case "log-in":
            log_in()

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
            admin_panel()