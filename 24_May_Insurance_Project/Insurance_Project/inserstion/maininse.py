import mysql.connector as connection
try:
    mydb = connection.connect(host = 'locaost',username = 'root',passwd = 'mysql',database = 'INSURANCE_PROJ')
    cur = mydb.cursor()
    print("DataBase Connected")
except:    
    print("DB not connected")