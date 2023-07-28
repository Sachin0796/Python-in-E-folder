import cx_Oracle

def InsertRecord():
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    # print(con.version)
    cursor = con.cursor()
    cursor.execute("insert into employees(EMPLOYEE_ID, LAST_NAME, EMAIL, HIRE_DATE, JOB_ID) values (10, 'khanna', 'abc', '20-AUG-07', 'AD_PRES')")
    con.commit()    
    print("Record inserted successfully !")
    cursor.close()
    con.close()

def printRecords():
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    cursor = con.cursor()
    cursor.execute('select name from stores')
    # rows = cursor.fetchmany(10)
    rows = cursor.fetchmany(10)
    print(rows)
    cursor.close()
    con.close()


# InsertRecord()
printRecords()