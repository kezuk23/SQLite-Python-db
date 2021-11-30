import DBViewer as DBViewer
import DBOperations as DBOperations
import Employee as Employee
import Formatcheck as Formatcheck


class DBEdit:


  def insert_data(self):

    try:
      # creating Employee and DBOperations objects
      emp = Employee.Employee()
      db_ops = DBOperations.DBOperations()
      format_check = Formatcheck.Formatcheck()
      #open db connection
      db_ops.get_connection()
      print("\n***New Employee Setup***\n")
      print("Please follow the instructions:")

      # method to autoincrement employeeID 
      # find out the largest number of employeeID if it exists
      largestID = db_ops.cur.execute(db_ops.sql_largest_employeeID)\
                                     .fetchone()
      if largestID[0] == None:
        nextIDinput = 1
      else: 
        nextIDinput=largestID[0]+1
      print("\nNew Employee Number: \t"+str(nextIDinput))
      
      #set all non-optional fields
      emp.set_employee_id(nextIDinput)
      emp.set_end_date('NULL')
      # all other fields - user options
      emp.set_title(input("Enter Employee Title: \t"))
      emp.set_forename(input("Enter Forename: \t\t"))
      emp.set_surname(input("Enter Surname: \t\t\t"))
      emp.set_email(input("Enter Email Address:\t"))
      salary = format_check.integer_check()
      emp.set_salary(salary)
      # emp.set_salary(input("Enter Salary: \t\t\t"))
      
      date = format_check.start_date_check() #returns date
      emp.set_start_date(date)

      db_ops.cur.execute(db_ops.sql_insert,\
                         tuple(str(emp).split("\n")))
      # commit db changes
      db_ops.conn.commit()
      #print confirmation
      print("\n*** Employee Number "+str(emp.get_employee_id())
            +" ("+str(emp.get_forename())+" "
            +str(emp.get_surname())+") added successfully ***")

    except Exception as e:
      print(e)
    finally:
      # close db connection
      db_ops.conn.close()

  def update_data(self):

    try:
      # creating DBViewer, DBOperations, and Formatcheck objects
      db_ops = DBOperations.DBOperations()
      db_view = DBViewer.DBViewer()
      format_check = Formatcheck.Formatcheck()
      #open db connection
      db_ops.get_connection()
      
      print("\n***Update Employee Records***\n")
      # catch input exception
      try:
        employeeID = input("Enter Employee ID: ")
        db_ops.cur.execute(db_ops.sql_search,\
                           tuple(str(employeeID)))
      except Exception:
        print("\nInvalid input, returning to Main Menu...") 
        return
      # display user selected
      db_view.display_employee(employeeID)

      # SUBMENU OPTIONS
      print("\nWhat would you like to update?\n")
      print(" 1. Employee name change")
      print(" 2. Employee email change")
      print(" 3. Employee salary change")
      print(" 4. Resignations and retirement")
      print(" 5. Entire employee record\n")
      selection = input("Selection: ")

      print("\n***Database editing mode***\n")
      if selection == '1':
        # editing names
        forename = input("Enter new forename: ")
        surname = input("Enter new surname: ")
        db_ops.cur.execute(db_ops.sql_update_name,\
        (forename, surname, employeeID))
      elif selection == '2': 
        # editing email address
        email = input("Enter new email: ")
        db_ops.cur.execute(db_ops.sql_update_email,\
        (email, employeeID))
      elif selection == '3':
        # editing salary
        salary = input("Enter new salary: ")
        db_ops.cur.execute(db_ops.sql_update_salary,\
        (salary, employeeID))
      elif selection == '4':
        # editing enddate
        enddate = format_check.end_date_check()
        db_ops.cur.execute(db_ops.sql_update_enddate,\
        (enddate, employeeID))
      elif selection == '5':
        # editing all
        title = input("New Title:\t\t\t")
        forename = input("New Forename:\t\t")
        surname = input("New Surname:\t\t")
        email = input("New Email:\t\t\t")
        salary = input("New Salary:\t\t\t")
        startdate = input("New start date:\t\t")
        db_ops.cur.execute(db_ops.sql_update_all,\
        (title, forename, surname, email,\
         salary, startdate, employeeID))
      else:
        print("Invalid selection.")
        return
      # last chance to cancel changes
      confirm = input("\nPress Y to confirm:\n")
      if confirm == 'Y' or confirm == 'y':
        # commit to db 
        db_ops.conn.commit()
        print("*** Database updated ***\n")
        # display updated record
        print("Updated record:")
        db_view.display_employee(employeeID)
      else:
        # disregard and return to menu
        print("Changes disregarded.")

    except Exception as e:
      print(e)
    finally:
      # close db connection
      db_ops.conn.close()

  def delete_data(self):

    try:
      # creating DBViewer and DBOperations objects
      db_ops = DBOperations.DBOperations()
      db_view = DBViewer.DBViewer()
      #open db connection
      db_ops.get_connection()

      print("\n***DELETE MENU***\n")
      print("WARNING - Deleted data cannot be recovered.\n")
      print("Type any letter now to cancel.\n")
      
      try:
        #catching input errors
        employeeID = int(input("Enter Employee ID: "))
        db_ops.cur.execute(db_ops.sql_search,\
                           tuple(str(employeeID)))
      except Exception:
        print("\nCancelled. Returning to Main Menu...")
        return

      result = db_ops.cur.fetchone()
      if result == None:
        print("\nUser not found.")
        return
      # show the selected record
      print("\nRecord selected:")
      db_view.display_employee(employeeID)
      
      print("\n*Deleting a record is permanent, all data is removed.")
      print("*Records can be retired using option 5 on Main Menu.")
      print("\nAre you sure you wish to delete?")
      
      choice = input("\nType Y to confirm (any other key to cancel): ")
      if choice == 'Y' or choice == 'y':
        # delete statement 
        db_ops.cur.execute(db_ops.sql_delete_data,\
                           tuple(str(employeeID)))
        # confirmation and commit
        print("\nEmployee "+ str(employeeID) +" deleted from database.\n")
        db_ops.conn.commit()
        print("***Database updated***")
      else:
        print("\nCancelled. Returning to Main Menu...")

    except Exception as e:
      print(e)
    finally:
      # close db connection
      db_ops.conn.close()
      