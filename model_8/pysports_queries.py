#Tatyana Romanova 
#07/21/2023
#8.2 Module / 4.MySQL pysports Query

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

    cursor = db.cursor()

    #select a query from the team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    #get the results from cursor
    teams = cursor.fetchall()

    print("\n -- DISPLAYING TEAM RECORDS --")

    #for loop to display results
    for team in teams:
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0],team[1],team[2]))

    #select a query from the player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    #get the results from the cursor
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")

    #for loop to display the results
    for player in players:
        print("  Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0],player[1],player[2], player[3]))

    input("\n\n  Pres any key to continue... ")    

#except block to handle errors
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
