import sqlite3
import pandas as pd
try:
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    print("Database created and Successfully Connected to SQLite")
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)

'''
    Write a query that returns the HomeTeam, FTHG (number of home goals scored in a game) and FTAG (number of away goals scored in a game)
    from the Matches table. Only include data from the 2010 season and where ‘Aachen’ is the name of the home team.
    Return the results by the number of home goals scored in a game in descending order.
'''

def qn_1():
    qn_1_query = pd.read_sql_query("""
    SELECT HomeTeam , FTHG , FTAG FROM Matches 
    WHERE Season = 2010 AND HomeTeam = 'Aachen' 
    ORDER BY FTHG DESC""",con)
    df = pd.DataFrame(qn_1_query)
    print(df)

'''
    Print the total number of home games each team won during the 2016 season in descending order of number of home games from the Matches table.
'''

def qn_2():
    qn_2_query = pd.read_sql_query('''
    SELECT  HomeTeam, COUNT(FTR) AS Home_Ground_Wins 
    FROM Matches WHERE Season = 2016 AND FTR = 'H'  
    GROUP BY HomeTeam ORDER BY COUNT(FTR) DESC ''',con)
    df = pd.DataFrame(qn_2_query)
    print(df)



'''
Write a query that returns the first ten rows from the Unique_Teams table
'''

def qn_3():
    qn_3_query = pd.read_sql_query("""
    SELECT * 
    FROM Unique_Teams 
    LIMIT 10""",con)
    df = pd.DataFrame(qn_3_query)
    print(df)

'''
    Print the Match_ID and Unique_Team_ID with the corresponding Team_Name from the Unique_Teams and Teams_in_Matches tables.
    Use the WHERE statement first and then use the JOIN statement to get the same result.
'''

'''
Using WHERE Statement
'''

def qn_4():
    qn_4_query = pd.read_sql_query("""
    SELECT *
    FROM Teams_in_Matches,Unique_Teams
    WHERE Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID 
    LIMIT 50""",con)
    df = pd.DataFrame(qn_4_query)
    print(df)

'''
Using Join Statement
'''

def qn_4_():
    qn_4_query = pd.read_sql_query("""
    SELECT *
    FROM Teams_in_Matches
    JOIN Unique_Teams
    ON Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID 
    LIMIT 50""",con)
    df = pd.DataFrame(qn_4_query)
    print(df)

'''
Write a query that joins together the Unique_Teams data table and the Teams table, and returns the first 10 rows.
'''
def qn_5():
    qn_5_query = pd.read_sql_query("""
    SELECT Unique_Teams.Unique_Team_ID,Unique_Teams.TeamName,Teams.KaderHome,Teams.AvgAgeHome,Teams.ForeignPlayersHome,Teams.OverallMarketValueHome,Teams.AvgMarketValueHome,Teams.StadiumCapacity
    FROM Unique_Teams 
    JOIN Teams
    ON Unique_Teams.TeamName = Teams.TeamName
    LIMIT 10""",con)
    df = pd.DataFrame(qn_5_query)
    print(df)

'''
    Write a query that shows the Unique_Team_ID and TeamName from the Unique_Teams table and AvgAgeHome, Season and ForeignPlayersHome from the Teams table.
    Only return the first five rows.
'''

def qn_6():
    qn_6_query = pd.read_sql_query("""
    SELECT Unique_Teams.Unique_Team_ID,Unique_Teams.TeamName,Teams.AvgAgeHome,Teams.Season,Teams.ForeignPlayersHome
    FROM Unique_Teams
    JOIN Teams
    On Unique_Teams.TeamName = Teams.TeamName
    LIMIT 5""",con)
    df = pd.DataFrame(qn_6_query)
    print(df)


'''
    Write a query that shows the highest Match_ID for each team that ends in a “y” or a “r”. Along with the maximum Match_ID,
    display the Unique_Team_ID from the Teams_in_Matches table and the TeamName from the Unique_Teams table.
'''

def qn_7():
    qn_7_query = pd.read_sql_query("""
    SELECT MAX(Teams_in_Matches.Match_ID) AS Highest_Match_ID, Teams_in_Matches.Unique_Team_ID, Unique_Teams.TeamName
    FROM Teams_in_Matches
    JOIN Unique_Teams
    ON  Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID
    WHERE (TeamName LIKE '%y') OR (TeamName LIKE '%r')
    GROUP BY Teams_in_Matches.Unique_Team_ID,TeamName
    """,con)
    df = pd.DataFrame(qn_7_query)
    print(df)


def request():
    print('\n')
    print("Choose anyone of the values")
    print("#" * 30)
    print("""
    Write a query that returns the HomeTeam, FTHG (number of home goals scored in a game) and FTAG (number of away goals scored in a game)
    from the Matches table. Only include data from the 2010 season and where ‘Aachen’ is the name of the home team.
    Return the results by the number of home goals scored in a game in descending order. ----> 1\n
    Print the total number of home games each team won during the 2016 season in descending order of number of home games from the Matches table. ----> 2\n
    Write a query that returns the first ten rows from the Unique_Teams table. ----> 3\n
    Print the Match_ID and Unique_Team_ID with the corresponding Team_Name from the Unique_Teams and Teams_in_Matches tables.
    Use the WHERE statement first and then use the JOIN statement to get the same result. ----> 4\n
    Write a query that joins together the Unique_Teams data table and the Teams table, and returns the first 10 rows. ----> 5\n
    Write a query that shows the Unique_Team_ID and TeamName from the Unique_Teams table and AvgAgeHome, Season and ForeignPlayersHome from the Teams table.
    Only return the first five rows. ----> 6\n
    Write a query that shows the highest Match_ID for each team that ends in a “y” or a “r”. Along with the maximum Match_ID,
    display the Unique_Team_ID from the Teams_in_Matches table and the TeamName from the Unique_Teams table. ----> 7
    """)
    try:
        choice = int(input("Choice: "))
        if choice in [1,2,3,4,5,6,7]:
            if choice == 1:
                qn_1()
            elif choice == 2:
                qn_2()
            elif choice == 3:
                qn_3()
            elif choice == 4:
                qn_4()
                qn_4_()
            elif choice == 5:
                qn_5()
            elif choice == 6:
                qn_6()
            else:
                qn_7()
    except:
        print("Sorry not a valid choice!!")
        request()
    rep = input("Do you have anymore Query [y/n]: ")
    if rep in ['y', 'Y']:
        request()
    elif rep in ['n','N']:
        exit()

    con.close()
if __name__ == "__main__":
    request()
