import sqlite3 #imports sqlite3 library
import time
import hashlib

#connecting to the database
db = sqlite3.connect("L4HDPGF2-E1.db")
db.row_factory = sqlite3.Row
query = db.cursor()


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
    
    user_available = False
    
    while user_available == False:
        username = input("\nWhat would you like your username to be?")
        
        sql = f"""
            SELECT username 
            FROM profiles
            WHERE username = {username};
            """
        
        rows
        for row in query.execute(sql):
            rows += 1
        
        if rows >= 1:
            print("\nSorry this username is not available.")
        else:
            #THIS IS NOT FINISHED
            sql = f"""
                INSERT INTO profiles()
            """
            
            print("\nAccount successfuly created!")

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
        return(True)

#hash the inputted message
def hash(message_in):
    m = hashlib.new("sha256")
    m.update(message_in.encode())
    return(m.hexdigest())

def modify_admin():
    add_or_remove = input("Enter 1 for add and 0 for remove to return press enter: ")
    user_email_addr = input("Input the users email address: ")
    
    if add_or_remove != 1 or 0:
        pass

    sql = f"""
            INSERT INTO accounts(administrator)
            VALUES("{add_or_remove}")
            WHERE email_address = {user_email_addr};
            """

    query.execute(sql)
    db.commit()