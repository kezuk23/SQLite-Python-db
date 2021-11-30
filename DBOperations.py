import sqlite3


class DBOperations:


  #LIST OF SQLite OPERATIONS IN ORDER OF MENU
  sql_create_table_firsttime = """CREATE TABLE IF NOT EXISTS Employees (
                                  employeeID INTEGER UNIQUE PRIMARY KEY, 
                                  title VARCHAR(5),
                                  forename VARCHAR(20),
                                  surname VARCHAR(20),
                                  email VARCHAR(20),
                                  salary INTEGER,
                                  startdate INTEGER,
                                  enddate INTEGER)"""

  sql_create_table = """CREATE TABLE Employees (
                        employeeID INTEGER UNIQUE PRIMARY KEY, 
                        title VARCHAR(5),
                        forename VARCHAR(20),
                        surname VARCHAR(20),
                        email VARCHAR(20),
                        salary INTEGER,
                        startdate INTEGER,
                        enddate INTEGER)"""
  
  # DISPLAY RECORDS
  sql_select_all = """SELECT * 
                      FROM Employees 
                      ORDER BY employeeID ASC"""

  sql_select_current = """SELECT employeeID, 
                                 forename, 
                                 surname, 
                                 email,
                                 salary, 
                                 startdate
                            FROM Employees 
                            WHERE enddate = 'NULL'"""

  sql_select_previous = """SELECT employeeID, 
                                  title, 
                                  forename, 
                                  surname,
                                  startdate, 
                                  enddate
                             FROM Employees 
                             WHERE enddate != 'NULL'"""

  sql_select_seniority = """SELECT employeeID, 
                                   forename, 
                                   surname, 
                                   startdate
                              FROM Employees 
                              WHERE enddate = 'NULL' 
                              ORDER BY startdate ASC"""

  sql_highest_salary = """SELECT * FROM
                          (SELECT MAX(salary) AS 'Highest Earner',
                                  forename,
                                  surname
                          FROM Employees
                          WHERE enddate = 'NULL')"""

  sql_average_salary = """SELECT * FROM
                         (SELECT AVG(salary) AS 'Average Salary'
                          FROM Employees
                          WHERE enddate = 'NULL')"""

  sql_total_salary = """SELECT * FROM 
                        (SELECT SUM(salary) AS 'Total Salary Expenditure'
                        FROM Employees
                        WHERE enddate = 'NULL')"""

  # INSERT RECORD
  sql_insert = """INSERT INTO Employees (
                              employeeID, 
                              title, 
                              forename, 
                              surname, 
                              email,
                              salary, 
                              startdate, 
                              enddate )
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

  # DELETE RECORDS
  sql_delete_data = """DELETE FROM Employees 
                       WHERE EmployeeID = ?"""

  # UPDATE RECORDS
  sql_update_name = """UPDATE Employees 
                       SET forename = ?, 
                           surname = ?
                       WHERE EmployeeID = ?"""

  sql_update_email = """UPDATE Employees 
                        SET email = ?
                        WHERE EmployeeID = ?"""

  sql_update_salary = """UPDATE Employees 
                         SET salary = ?
                         WHERE EmployeeID = ?"""

  sql_update_enddate = """UPDATE Employees 
                          SET enddate = ?
                          WHERE EmployeeID = ?"""

  sql_update_all = """UPDATE Employees
                      SET title = ?, 
                          forename = ?, 
                          surname = ?,
                          email = ?, 
                          salary = ?, 
                          startdate = ?
                      WHERE EmployeeID = ?"""

  # SEARCH RECORDS
  sql_search = """SELECT * 
                  FROM Employees 
                  WHERE EmployeeID = ?"""

  # MISCELLANEOUS 
  sql_largest_employeeID = """SELECT MAX(employeeID) 
                            FROM Employees"""

  def __init__(self):

    try:
      self.conn = sqlite3.connect("Employees.db")
      self.cur = self.conn.cursor()
      self.cur.execute(self.sql_create_table_firsttime)
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def get_connection(self):

    self.conn = sqlite3.connect("Employees.db")
    self.cur = self.conn.cursor()

  # INITIALISE DATABASE - CREATE TABLE
  def create_table(self):

    try:
      self.get_connection()
      self.cur.execute(self.sql_create_table)
      self.conn.commit()
      print("Table created successfully.")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()
      