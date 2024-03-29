import sqlite3 #imports sqlite3 library
import time
import hashlib

#connecting to the database
db = sqlite3.connect("L4HDPGF2-E1.db")
db.row_factory = sqlite3.Row
query = db.cursor()

current_UUID = 0


def sign_up():
    email_addr = input("\nEmail address: ")
    password = input("\nPassword: ")

    passwd_hash = hash(password)

    sql = f"""
            INSERT INTO accounts(email_address, password_hash, social_credit, administrator, days_since_login)
            VALUES("{email_addr}", "{passwd_hash}", 1000, 0, 0);
            """

    query.execute(sql)
    db.commit()
    
    user_available = False
    
    while user_available == False:
        username = input("\nWhat would you like your username to be?: ")
        
        sql = f"""
            SELECT username 
            FROM profiles
            WHERE username = '{username}';
            """
        
        rows = 0
        
        for row in query.execute(sql):
            rows = rows + 1
        
        if rows >= 1:
            print("\nSorry this username is not available.")
        else:
            sql = f"""
            SELECT UUID
            FROM accounts
            WHERE email_address = '{email_addr}';
            """
            
            #This works but it's dodgy
            for row in query.execute(sql):
                current_UUID = row['UUID']

            sql = f"""
                INSERT INTO profiles(UUID, username)
                VALUES({current_UUID}, '{username}')
            """
            query.execute(sql)
            db.commit()
            
            print("\nAccount successfuly created!")

def log_in():
    global current_UUID
    email_addr = input("\nEmail address: ")
    password = input("\nPassword: ")

    passwd_hash = hash(password)

    sql = f"""
            SELECT UUID, password_hash, administrator
            FROM accounts
            WHERE email_address = "{email_addr}";
            """
    
    for row in query.execute(sql):
        resulst = [row['UUID'], row['password_hash'], row['administrator']]
    
    if passwd_hash == resulst[1]:
        print("\nLogin successful!")
    
    current_UUID = resulst[0]
    
    if resulst[2] == 1:
        return(True)

#hash the inputted message
def hash(message_in):
    m = hashlib.new("sha256")
    m.update(message_in.encode())
    return(m.hexdigest())

def get_admin():
    
    username = input("\nEnter the users username: ")

    sql = f"""
        SELECT accounts.administrator
        FROM accounts, profiles
        WHERE profiles.username = "{username}"
        AND accounts.UUID = profiles.UUID;
    """
    
    for row in query.execute(sql):
        if row['administrator'] == 1:
            print(f"\n{username} is an administrator.")
        else:
            print(f"\n{username} is not an adminstrator.")

def modify_admin():
    add_or_remove = int(input("\nEnter 1 for add and 0 for remove to return press enter: "))
        
    if add_or_remove != 1 and add_or_remove != 0:
        print("\nThat is not an option!")
        pass

    username = input("Input the users username: ")

    sql = f"""
        UPDATE accounts
        SET administrator = {add_or_remove}
        FROM profiles
        WHERE profiles.username = "{username}"
        AND accounts.UUID = profiles.UUID;
        """

    query.execute(sql)
    db.commit()

    #I am going insane this is starting to look like valve dev comments
    print("\nBye bye administrator!!!")

def change_class():
    yet_to_choose = True
    chosen_class = 0
    
    #I could have probably just done a query for this lmao
    while yet_to_choose == True:
        chosen_class = input("\nWhat class would you like to use? (Type !help for options): ")
        match chosen_class:
            case "!help":
                print("\Classes: \nGordon Freeman \nAdrian Shephard \nBarney Calhoun \nAlyx Vance \nG-Man \nScout \nSoldier \nPyro \nDemoman \nHeavy \nEngineer \nMedic \nSniper \nSpy \nChell \nGLaDOS \nWheatley")
            case "Gordon Freeman":
                chosen_class = 1
                yet_to_choose = False
            case "Adrian Shephard":
                chosen_class = 2
                yet_to_choose = False
            case "Barney Calhoun":
                chosen_class = 3
                yet_to_choose = False
            case "Alyx Vance":
                chosen_class = 4
                yet_to_choose = False
            case "G-Man":
                chosen_class = 5
                yet_to_choose = False
            case "Scout":
                chosen_class = 6
                yet_to_choose = False
            case "Soldier":
                chosen_class = 7
                yet_to_choose = False
            case "Pyro":
                chosen_class = 8
                yet_to_choose = False
            case "Demoman":
                chosen_class = 9
                yet_to_choose = False
            case "Heavy":
                chosen_class = 10
                yet_to_choose = False
            case "Engineer":
                chosen_class = 11
                yet_to_choose = False
            case "Medic":
                chosen_class = 12
                yet_to_choose = False
            case "Sniper":
                chosen_class = 13
                yet_to_choose = False
            case "Spy":
                chosen_class = 14
                yet_to_choose = False
            case "Chell":
                chosen_class = 15
                yet_to_choose = False
            case "GLaDOS":
                chosen_class = 16
                yet_to_choose = False
            case "Wheatley":
                chosen_class = 17
                yet_to_choose = False
    
    sql = f"""
            UPDATE profiles
            SET class_ID = '{chosen_class}'
            WHERE UUID = {current_UUID};
            """
    query.execute(sql)
    db.commit()
    
    print("\nClass changed successfuly!")

def get_class():
    class_name = ""
    
    sql = f"""
        SELECT classes.class_name
        FROM profiles, classes
        WHERE UUID = "{current_UUID}"
        AND profiles.class_ID = classes.class_ID;
        """
    
    for row in query.execute(sql):
        class_name = row['class_name']
    
    print(f"\nYour current selected class is '{class_name}'")

def get_user():
    return(current_UUID)

#removes every player who hasn't logged in for 365 days because people don't deserve the right to keep the things they bought with their hard earned money
def ubisoft():
    sql = f"""
        DELETE FROM accounts
        WHERE days_since_login >= 365;
        """
    
    query.execute(sql)
    db.commit()
    
    print("\nAhh yes I love taking away peoples rights!")