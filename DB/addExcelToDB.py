import sqlite3
import openpyxl
#Will create db if not found
#sent = "this sdfsdfzxczxzxc first ques"

def connect() :
    try:
        con = sqlite3.connect('slackbot.db')
        c = con.cursor()
    except :
        print('DB Connection ERROR : ')

    return con,c

def add() :
    try:
        con,c = connect()
        c.execute('''CREATE TABLE IF NOT EXISTS supportmatrix (osversion text,reldate text,comment text,iversion text,lversion text,sheet text)''')

        wb = openpyxl.load_workbook('../OSVERSION/OS Release Dates.xlsx')
        x = wb.get_sheet_names()
        # print (x)
        for i in x:
            sh = wb.get_sheet_by_name(i)
            max_row = sh.max_row
            for j in range(2, max_row):
                if i != "Windows" :
                    os_name = i +" "+str(sh['A' + str(j)].value)
                else:
                    os_name = sh['A' + str(j)].value
                rel_date = sh['B' + str(j)].value
                if rel_date == '??':
                    rel_date =None
                comment = sh['C' + str(j)].value
                if comment == None:
                    comment=''
                i_version = sh['D' + str(j)].value
                if i_version == None:
                    i_version = ''
                l_version = sh['E' + str(j)].value
                if l_version == None:
                    l_version = ''
                sheet_name = i
                if not (os_name == None or rel_date == None ) and (
                        len(i_version) != 0 or len(l_version) != 0):
                    comment = str(comment)
                    print (str(os_name) + ', ' + str(
                        rel_date) + ', ' + comment + ', ' + i_version + ', ' + l_version + ', ' + sheet_name)
                    values = "'"+str(os_name)+"',"+"'"+str(rel_date)+"',"+"'"+comment+"',"+"'"+i_version+"',"+"'"+l_version+"',"+"'"+sheet_name+"'"
                    sql = "INSERT INTO supportmatrix VALUES ("+values+")"
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
        c.execute('''select * from supportmatrix''')
        exe = c.fetchall()
        for i in exe:
            print (i)
        con.commit()
    except:
        print("Fetch ERROR: ")
    finally:
        con.close()

add()