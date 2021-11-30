import DBOperations as DBOperations
import DBViewer as DBViewer
import DBEdit as DBEdit


class Main:
    

  # creating DBOperations, DBViewer, and DBEdit objects
  db_ops = DBOperations.DBOperations()
  db_viewer = DBViewer.DBViewer()
  db_edit = DBEdit.DBEdit()

  while True:
    print ("\n Main menu:")
    print (" **********")
    print (" 1. Initialise Employees database")
    print (" 2. Display Employees database")
    print (" 3. Add new Employees")
    print (" 4. Remove Employee records")
    print (" 5. Update existing records")
    print (" 6. Search Employees")
    print (" 7. Exit\n")
    
    try:
      __choose_menu = int(input("Enter your choice: "))
      
      if __choose_menu == 1:
        db_ops.create_table()
      elif __choose_menu == 2:
        db_viewer.select_all()
      elif __choose_menu == 3:
        db_edit.insert_data()
      elif __choose_menu == 4:
        db_edit.delete_data()
      elif __choose_menu == 5:
        db_edit.update_data()
      elif __choose_menu == 6:
        db_viewer.search_data()
      elif __choose_menu == 7:
        print("\n**Database closed.**")
        exit(0)
      else:
        print ("\nInvalid Choice.")
    except Exception:
      print("\n**Invalid Choice. Try again.**")
