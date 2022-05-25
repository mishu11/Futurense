query = """CREATE TABLE COMPANIES
(
	COMPANY_ID INT PRIMARY KEY AUTO_INCREMENT,
    COMPANY_NAME VARCHAR(100) NOT NUll
    
);"""
import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
cur = mydb.cursor()
cur.execute(query)