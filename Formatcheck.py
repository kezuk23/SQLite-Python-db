import datetime


class Formatcheck:


  def integer_check(self):
    intcheck = False
    while intcheck == False:
      try:
        salary = input("Enter Salary: \t\t\t")
        if salary.isdecimal() == True:
          intcheck = True
          break
        else:
          print("Not a valid number, try again")
      except Exception as e:
        print(e)
    return salary


  def start_date_check(self):
    dateinput = '0'
    while dateinput != '1' and dateinput != '2':
      dateinput = input("Select 1 for new hire, 2 for existing.\
                        \nEmployee status: \t\t")
      if dateinput == '1':
        # start date will be today's date
        x = datetime.datetime.now() 
        date = (x.strftime("%Y-%m-%d")) # to display YYYY-MM-DD format
      elif dateinput == '2':
        # start date can be any valid date
        datecheck = False
        print("Date format must be YYYY-MM-DD.")
        
        while datecheck == False:
          date = input("Enter hire date: \t\t")
          try:
            # date format check
            format = "%Y-%m-%d"
            datetime.datetime.strptime(date, format)
            datecheck = True
          except ValueError:
            print("\nInvalid date/format. Try again.")
            print("Required format: YYYY-MM-DD with dashes")
      else:
          print("Invalid choice.")
    return date

  def end_date_check(self):
    datecheck = False
    while datecheck == False:
      date = input("Enter final date of employment: ")
      try:
        # date format check
        format = "%Y-%m-%d"
        datetime.datetime.strptime(date, format)
        datecheck = True
      except ValueError:
        print("\nInvalid date/format. Try again.")
        print("Required format: YYYY-MM-DD with dashes")
    return date

