import sqlite3

#Will create db if not found
#sent = "this sdfsdfzxczxzxc first ques"

def connect() :
    try:
        con = sqlite3.connect('slackbot.db')
        c = con.cursor()
    except :
        print('DB Connection ERROR : ')

    return con,c

def add(sent) :
    try:
        con,c = connect()
        c.execute('''CREATE TABLE IF NOT EXISTS question (Ques text)''')
        sql = "INSERT INTO question (Ques) VALUES ('"+sent+"')"
        c.execute(sql)
#       c.execute('''select * from answered''')
#       print(c.fetchall())
        con.commit()
        con.close()
    except :
        print ("DB ERROR : ")
    finally:
        con.close()



def fetch() :
    try :
        con, c = connect()
        c.execute('''select * from question''')
        print(c.fetchall())
        con.commit()
    except:
        print("Fetch ERROR: ")
    finally:
        con.close()

def drop() :
    try:
        con,c = connect()
        c.execute('DROP TABLE question')
    except:
        print("DROP ERROR")


 ####test loclally#####
add(sent)
fetch()
#drop()