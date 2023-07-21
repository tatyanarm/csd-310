#Tatyana Romanova 
#07/21/2023
#8.2 Module / 4.MySQL connection Test

#import statements
import mysql.connector
from mysql.connector import errorcode

#database configure object
config = {
    "user": "pysports_user",
    "password": "Tatyana87#",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#try block for handling potential MySQL database errors
try:
    db = mysql.connector.connect(**config) #connect to the pysports database

    #output connection status
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" ~~ The supplied username or password are invalid ~~ ")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" ~~ The specified database does not exist ~~ ")

    else:
        print(err)

finally:
    #close the connection to MySQL
    db.close()
