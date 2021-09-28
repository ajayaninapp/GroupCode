import sqlite3


def connect_db(name):
    con = sqlite3.connect(name)
    return con


def create_table(cur):
    try:
        cur.execute("CREATE TABLE Departments (Department_Id INTEGER PRIMARY KEY, Department_Name VARCHAR(30))")
    except sqlite3.OperationalError:
        print("The table has already been created")


def insert_records(cur):
    try:
        cur.executemany('INSERT INTO Departments VALUES (?,?)',
                        [(1, 'Accounting'),
                         (2, 'Operations'),
                         (3, 'Human Resources'),
                         (4, 'Development'),
                         (5, 'IT Services')])
        print("Records inserted to Employee Table")
        connection.commit()
    except sqlite3.IntegrityError:
        print("Records have already been added to Employee Table")


def display_records(cur):
    cur.execute("SELECT * FROM Departments")
    print("Department_Id\tDepartment_Name")
    for item in cur.fetchall():
        print("{}\t\t\t\t{}".format(item[0], item[1]))


def modify_db(cur):
    try:
        cur.execute(
            "CREATE TABLE Employee1 (Name VARCHAR(30), Id INTEGER PRIMARY KEY, Salary INTEGER, Department_Id INTEGER , City VARCHAR(30), FOREIGN KEY(Department_Id) REFERENCES Departments(Department_Id))")
        connection.commit()
    except sqlite3.OperationalError:
        print("Already exists")
    cur.execute("INSERT INTO Employee1 SELECT * FROM Employee")
    connection.commit()
    cur.execute("DROP Table Employee")
    cur.execute("ALTER TABLE Employee1 RENAME TO Employee")
    connection.commit()


def search_department(cur):
    id_of_department = int(input("Enter Department ID : "))
    query1 = "SELECT Name,Id,Salary,Employee.Department_Id,City,Department_Name FROM Employee,Departments WHERE Employee.Department_Id=Departments.Department_Id and Departments.Department_Id=?"
    cur.execute(query1, (id_of_department,))
    result = cur.fetchall()
    if len(result) == 0:
        print("No records Found!!!")
    else:
        for item in result:
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(item[0], item[1], item[2], item[3], item[4], item[5]))


if __name__ == "__main__":
    connection = connect_db('EmployeeDB.db')
    cursor1 = connection.cursor()
    create_table(cursor1)
    insert_records(cursor1)
    display_records(cursor1)
    modify_db(cursor1)
    search_department(cursor1)
    connection.close()
