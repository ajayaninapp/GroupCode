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
Counts all the rows in the Teams table
'''

# def qn_1():
#     df = pd.read_sql("""
#     SELECT *
#     FROM Teams""", con)
#     print(len(df))

##########################################OR########################################

def qn_1():
    qn_1_query = pd.read_sql("""
    SELECT COUNT(*) AS Row_Count
    FROM Teams""", con)
    df = pd.DataFrame(qn_1_query)
    print(df)

'''
Print all the unique values that are included in the Season column in the Teams table
'''
# def qn_2():
#     qn_2_query = pd.read_sql("""
#     SELECT *
#     FROM Teams""",con)
#     df = pd.DataFrame(qn_2_query)
#     print(df.Season.unique())

##########################################OR########################################

def qn_2():
    qn_2_query = pd.read_sql("""
    SELECT DISTINCT Season 
    FROM Teams""",con)
    df = pd.DataFrame(qn_2_query)
    print(df)

'''
Print the largest and smallest stadium capacity that is included in the Teams table
'''
# def qn_3():
#     qn_3_query = pd.read_sql("""
#     SELECT StadiumCapacity
#     FROM Teams""",con)
#     df = pd.DataFrame(qn_3_query)
#     print(f"Maximum {df.max()} and Minimum {df.min()} ")

##########################################OR########################################

def qn_3():
    qn_3_query = pd.read_sql("""
    SELECT MAX(StadiumCapacity) AS Max_Stadium_Capacity , MIN(StadiumCapacity) AS Min_Stadium_Capacity
    FROM Teams""",con)
    df = pd.DataFrame(qn_3_query)
    print(df)

'''
Print the sum of squad players for all teams during the 2014 season from the Teams table [Answer - 1164]
'''

def qn_4():
    qn_4_query = pd.read_sql("""
    SELECT SUM(KaderHome) AS Total_Squad_Players
    FROM Teams 
    WHERE Season = 2014 """,con)
    df = pd.DataFrame(qn_4_query)
    print(df)

'''
Query the Matches table to know how many goals did Man United score during home games on average? [Answer - 2.16]
'''

def qn_5():
    qn_5_query = pd.read_sql("""
    SELECT ROUND(AVG(FTHG),2) AS Avg_Man_United_Score 
    FROM Matches 
    WHERE HomeTeam = 'Man United' """,con)
    df = pd.DataFrame(qn_5_query)
    print(df)

print("\tUSER REQUESTS")
print("#"*25)
def request():
    print('\n')
    print("Choose anyone of the values")
    print("#" * 30)
    print("""
    Counts all the rows in the Teams table----> 1\n
    Print all the unique values that are included in the Season column in the Teams table ----> 2\n
    Print the largest and smallest stadium capacity that is included in the Teams table ----> 3\n
    Print the sum of squad players for all teams during the 2014 season from the Teams table [Answer - 1164] ----> 4\n
    Query the Matches table to know how many goals did Man United score during home games on average? [Answer - 2.16] ----> 5\n
    """)
    try:
        choice = int(input("Choice: "))
        if choice in [1,2,3,4,5]:
            if choice == 1:
                qn_1()
            elif choice == 2:
                qn_2()
            elif choice == 3:
                qn_3()
            elif choice == 4:
                qn_4()
            else:
                qn_5()
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

