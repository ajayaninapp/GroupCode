import sqlite3
import pandas as pd

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)


try:
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    print("Database created and Successfully Connected to SQLite")
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)



'''
Print the names of both the Home Teams and Away Teams in each match played in 2015 and Full time Home Goals (FTHG) = 5
'''

# def qn_1(x,y):
#     qn_1_query = '''
#     SELECT HomeTeam , AwayTeam
#     FROM Matches WHERE Season =? AND FTHG = ? '''
#     cur.execute(qn_1_query,(x,y))
#     result1 = cur.fetchall()
#     print("The names of both the Home Teams and Away Teams in each match played in 2015 and Full time Home Goals (FTHG) = 5\n")
#     for row in result1:
#         print("Home Team = ", row[0])
#         print("AWAY TEAM = ", row[1],'\n')
#
# qn_1(2015,5)

def qn_1():
    print("The names of both the Home Teams and Away Teams in each match played in 2015 and Full time Home Goals ("
          "FTHG) = 5\n")
    qn_1_query = pd.read_sql_query('''
    SELECT HomeTeam , AwayTeam 
    FROM Matches 
    WHERE Season = 2015 AND FTHG = 5 ''', con)
    df = pd.DataFrame(qn_1_query)
    print(df)


'''
Print the details of the matches where Arsenal is the Home Team and  Full Time Result (FTR) is “A” (Away Win)
'''
# def qn_2(ht,ftr):
#     qn_2_query = '''
#     SELECT  Match_ID,Div,Season,Date,HomeTeam,AwayTeam,FTAG
#     FROM Matches
#     WHERE HomeTeam = ? AND FTR = ?'''
#     cur.execute(qn_2_query,(ht,ftr))
#     result2 = cur.fetchall()
#     print("The details of the matches where Arsenal is the Home Team and  Full Time Result (FTR) is “A” (Away Win)\n")
#     for row in result2:
#         print("MATCH ID = ",row[0])
#         print("DIV = ",row[1])
#         print("SEASON = ",row[2])
#         print("DATE = ", row[3])
#         print("Home Team = ", row[4])
#         print("Away Team = ", row[5])
#         print('Full Time Away Goal = ',row[6],'\n')
#
# qn_2("Arsenal","A")

def qn_2():
    print("The details of the matches where Arsenal is the Home Team and  Full Time Result (FTR) is “A” (Away Win)\n")
    qn_2_query = pd.read_sql_query('''
    SELECT  Match_ID,Div,Season,Date,HomeTeam,AwayTeam,FTAG 
    FROM Matches 
    WHERE HomeTeam = "Arsenal" AND FTR = "A"''',con)
    df = pd.DataFrame(qn_2_query)
    print(df)


'''
Print all the matches from the 2012 season till the 2015 season where Away Team is Bayern Munich and Full time Away Goals (FTHG) > 2
'''

# def qn_3():
#     qn_3_query = '''
#     SELECT HomeTeam,FTHG
#     FROM Matches
#     WHERE AwayTeam = 'Bayern Munich'
#     AND Season BETWEEN 2012 AND 2015 AND FTHG > 2 '''
#     cur.execute(qn_3_query)
#     result3 = cur.fetchall()
#     print("All the matches from the 2012 season till the 2015 season where Away Team is Bayern Munich and Full time Away Goals (FTHG) > 2\n")
#     for row in result3:
#         print(row[0],"Vs",'Bayern Munich')
#         print("Full Time Half Goal = ",row[1],'\n')
# qn_3()

def qn_3():
    print("All the matches from the 2012 season till the 2015 season where Away Team is Bayern Munich and Full time Away Goals (FTHG) > 2\n")
    qn_3_query = pd.read_sql_query('''
    SELECT HomeTeam,FTHG FROM Matches 
    WHERE AwayTeam = 'Bayern Munich' 
    AND Season BETWEEN 2012 AND 2015 AND FTAG > 2 ''',con)
    df = pd.DataFrame(qn_3_query)
    print(df)


'''
Print all the matches where the Home Team name begins with “A” and Away Team name begins with “M”
'''

# def qn_4():
#     qn_4_query = '''
#     SELECT HomeTeam,AwayTeam
#     FROM Matches
#     WHERE HomeTeam
#     LIKE 'A%' AND AwayTeam LIKE 'M%' '''
#     cur.execute(qn_4_query)
#     result4 = cur.fetchall()
#     print("All the matches where the Home Team name begins with “A” and Away Team name begins with “M”\n")
#     for row in result4:
#         print(row[0],'Vs',row[1],'\n')
#
# qn_4()


def qn_4():
    print("All the matches where the Home Team name begins with “A” and Away Team name begins with “M”\n")
    qn_4_query = pd.read_sql_query('''
    SELECT HomeTeam,AwayTeam 
    FROM Matches WHERE HomeTeam 
    LIKE 'A%' AND AwayTeam LIKE 'M%' ''',con)
    df =pd.DataFrame(qn_4_query)
    print(df)

print("\tUSER REQUESTS")
print("#"*25)
def request():
    print('\n')
    print("Choose anyone of the values")
    print("#" * 30)
    print("""
    Print the names of both the Home Teams and Away Teams in each match played in 2015 and Full time Home Goals (FTHG) = 5 ----> 1\n
    Print the details of the matches where Arsenal is the Home Team and  Full Time Result (FTR) is “A” (Away Win) ----> 2\n
    Print all the matches from the 2012 season till the 2015 season where Away Team is Bayern Munich and Full time Away Goals (FTHG) > 2 ----> 3\n
    All the matches where the Home Team name begins with “A” and Away Team name begins with “M” ----> 4\n""")
    try:
        choice = int(input("Choice: "))
        if choice in [1,2,3,4]:
            if choice == 1:
                qn_1()
            elif choice == 2:
                qn_2()
            elif choice == 3:
                qn_3()
            else:
                qn_4()
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




