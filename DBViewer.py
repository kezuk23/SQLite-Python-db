import pandas as pd
import DBOperations as DBOperations


class DBViewer: 


  def select_all(self):

      try:
        # creating DBOperations object
        db_ops = DBOperations.DBOperations()
        #open db connection
        db_ops.get_connection()

        # Using pandas to display the data in tabular format
        # pandas settings
        pd.set_option('display.width', 100)
        pd.set_option('display.max_columns', 8)

        # SUB-MENU OPTIONS
        print ("\n Display Menu:")
        print (" **********")
        print(" What would you like to display?")
        print(" 1. Entire database")
        print(" 2. Current employees")
        print(" 3. Seniority list")
        print(" 4. Previous employees")
        print(" 5. Current salary metrics\n")

        select = input("Enter your choice: ")
        if select == '1':
          print("\nEmployees Database:\n")
          print(pd.read_sql_query(db_ops.sql_select_all,\
                db_ops.conn))
        elif select == '2':
          print("\nCurrent Employees:\n")
          print(pd.read_sql_query(db_ops.sql_select_current,\
                db_ops.conn))
        elif select == '3':
          print("\nSeniority List:\n")
          print(pd.read_sql_query(db_ops.sql_select_seniority,\
                db_ops.conn))
        elif select == '4':
          print("\nFormer Employees:\n")
          print(pd.read_sql_query(db_ops.sql_select_previous,\
                db_ops.conn))
        elif select == '5':
          print("\n**Live Salary Metrics**\n")
          # average salary of current employees
          select1 = (db_ops.cur.execute(db_ops.sql_average_salary)\
                    .fetchone())
          # round to two decimal places
          roundedselect1 = round(select1[0], 2)
          print("Current average salary: \t"+str(roundedselect1))
          # highest earner in current employees
          select2 = db_ops.cur.execute(db_ops.sql_highest_salary)\
                    .fetchone()
          fullselect2 = (str(select2[1])+" "+str(select2[2])+", "\
                        +str(select2[0]))
          print("Current highest earner: \t"+str(fullselect2))
          # total outgoings for current employees
          select3 = db_ops.cur.execute(db_ops.sql_total_salary)\
                    .fetchone()
          print("Total salary expenditure: \t"+str(select3[0]))
          
        else:
          print("\nInvalid choice. Returning to Main Menu...")
      except Exception as e:
        print(e)
      finally:
        # close db connection
        db_ops.conn.close()

  def search_data(self):

    try:
      # creating DBOperations object
      db_ops = DBOperations.DBOperations()
      # open db connection
      db_ops.get_connection()
      print("\n**Search Employees**\n")
      employeeID = int(input("Enter Employee ID: "))
      try: 
        # using try block in case empID doesn't exist 
        DBViewer.display_employee(self, employeeID)
      except Exception as e1:
        print(e1)
      
    except Exception:
      print("\nInput Error. Returning to Main Menu...")
    finally:
      # close db connection
      db_ops.conn.close()

  # def display_employee(db_ops, employeeID):
  def display_employee(self, employeeID):
    try:
      # creating DBOperations object
      db_ops = DBOperations.DBOperations()
      # open db connection
      db_ops.get_connection()
      result = db_ops.cur.execute(db_ops.sql_search,\
               tuple(str(employeeID))).fetchone()
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("\nEmployee ID: \t\t" + str(detail))
          elif index == 1:
            print("Employee Title: \t" + detail)
          elif index == 2:
            print("Employee Forename: \t" + detail)
          elif index == 3:
            print("Employee Surname: \t" + detail)
          elif index == 4:
            print("Employee Email: \t" + detail)
          elif index == 5:
            print("Salary: \t\t\t"+ str(detail))
          elif index == 6:
            print("Date Started: \t\t" + str(detail))
          elif index == 7:
            print("Date Left: \t\t\t" + str(detail))
      else:
        print ("\nNo Record.")

    except Exception as e:
      print(e)
    finally:
      # close db connection
      db_ops.conn.close()
      