import sqlite3


def connect_db(name):
    con = sqlite3.connect(name)
    return con


def create_table(cur):
    try:
        cur.execute(
            "CREATE TABLE Employee (Name VARCHAR(30), Id INTEGER PRIMARY KEY, Salary INTEGER, Department_Id INTEGER)")
    except sqlite3.OperationalError:
        print("The table has already been created")


def add_column_city(cur):
    try:
        cur.execute("ALTER TABLE Employee ADD City VARCHAR(30)")
        print("Column City Added to Table Employee")
        connection.commit()
    except sqlite3.OperationalError:
        print("Column City has been added to Table Employee")


def insert_records(cur):
    try:
        cur.executemany('INSERT INTO Employee VALUES (?,?,?,?,?)',
                        [('Sheldon', 101, 35000, 1, 'London'),
                         ('Richard', 102, 40000, 2, 'New York'),
                         ('Susan', 103, 38000, 3, 'Tokyo'),
                         ('Robert', 104, 32000, 3, 'Tokyo'),
                         ('Linda', 105, 35000, 1, 'London')])
        print("Records inserted to Employee Table")
        connection.commit()
    except sqlite3.IntegrityError:
        print("Records have already been added to Employee Table")


def display_employee_details(cur):
    cur.execute('SELECT Name,Id,Salary FROM Employee')
    print("Name\tId\tSalary")
    for item in cur.fetchall():
        print("{}\t{}\t{}".format(item[0], item[1], item[2]))


def search_employee_with_letter(cur):
    start_letter = input("Enter the letter to search with : ").capitalize()
    search_string = start_letter + '%'
    query1 = "SELECT * FROM Employee WHERE Name LIKE ?"
    cur.execute(query1, (search_string,))
    result1 = cur.fetchall()
    if len(result1) == 0:
        print("Name does not exist!!!")
    else:
        for item in result1:
            print("{}\t{}\t{}\t{}\t{}".format(item[0], item[1], item[2], item[3], item[4]))


def search_employee_with_id(cur):
    while True:
        try:
            id_of_employee = int(input("Enter the ID of the Employee to search for : "))
            query2 = "SELECT * FROM Employee WHERE Id=?"
            cur.execute(query2, (id_of_employee,))
            result2 = cur.fetchall()
            if len(result2) == 0:
                print("Employee not Found!!!")
                continue
            else:
                print("Name\tID\tSalary\tDepartment_ID\tCity")
                print(
                    "{}\t{}\t{}\t{}\t\t\t\t{}".format(result2[0][0], result2[0][1], result2[0][2], result2[0][3],
                                                      result2[0][4]))
        except ValueError:
            print("Invalid Value!!!")
        else:
            break


def change_employee_name(cur):
    try:
        name_change_id = int(input("Enter Id of Employee whose name is to be changed : "))
        new_name = input("Enter new name for the Employee : ")
        query3 = "UPDATE Employee SET Name=? WHERE Id=?"
        cur.execute(query3, (new_name, name_change_id))
        print("Name Changed Successfully")
        connection.commit()
    except ValueError:
        print("Invalid Value!!!")


if __name__ == "__main__":
    connection = connect_db('EmployeeDB.db')
    cursor1 = connection.cursor()
    create_table(cursor1)
    add_column_city(cursor1)
    insert_records(cursor1)
    display_employee_details(cursor1)
    search_employee_with_letter(cursor1)
    search_employee_with_id(cursor1)
    change_employee_name(cursor1)
    display_employee_details(cursor1)
    connection.close()
