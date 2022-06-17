import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="TdR"
) 

command_history = []
ant_command = None
num = 0

while True:
    conn = sqlite3.connect(db)

    c = conn.cursor()
    if not ant_command == None:
        sql = input("    >> "+ant_command)
    else: 
        sql = input("    >> ")

    if sql == "e" or sql == "exit":
        break
    if sql == "u" or sql == "up":
        try:
            num += 1
            ant_command = command_history[len(command_history)-1-num]
        except IndexError:
            print("That was the last command")
            num -= 1
    elif sql == "d" or sql == "down":
        num = num - 1 if not num == 0 else 0
        ant_command = command_history[len(command_history)-1-num] if not num == 0 else None
    elif sql == "" and not ant_command == None:
        temp = c.execute(ant_command)
        res = temp.fetchall()
        print(res)
        conn.commit()
        command_history.append(ant_command)
        num = 0
        ant_command = None
    else:
        try:
            temp = c.execute(sql)
            res = temp.fetchall()
            print(res)
            conn.commit()
            num = 0
            command_history.append(sql)
            ant_command = None
        except Exception as e:
            print(e)
conn.close()
