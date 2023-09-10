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