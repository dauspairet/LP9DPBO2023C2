import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_pywiki",
)

dbcursor = mydb.cursor()

sql1 = "INSERT INTO game(game_nama, game_genre) VALUES (%s, %s)"
val1 = ("Resident evil 4 Remake", "Horror")
sql2 = "INSERT INTO game(game_nama, game_genre) VALUES (%s, %s)"
val2 = ("Battlefield 1", "FPS")
dbcursor.execute(sql1, val1)
dbcursor.execute(sql2, val2)

mydb.commit()

print(dbcursor.rowcount, "record inserted.")

# Print all records
sql_print = "SELECT * FROM game"
dbcursor.execute(sql_print)
result = dbcursor.fetchall()

for row in result:
    print("ID   :", row[0])
    print("Game :", row[1])
    print("Genre:", row[2])
    print("------------")
