

class Employee:


  def __init__(self):
    
    self.employeeID = 1
    self.title = ''
    self.forename = ''
    self.surname = ''
    self.email = ''
    self.salary = 0
    self.startdate = ''
    self.enddate = ''

  def set_employee_id(self, employeeID):
    self.employeeID = employeeID

  def set_title(self, title):
    self.title = title

  def set_forename(self,forename):
   self.forename = forename
  
  def set_surname(self,surname):
    self.surname = surname

  def set_email(self,email):
    self.email = email
  
  def set_salary(self,salary):
    self.salary = salary

  def set_start_date(self,startdate):
    self.startdate = startdate

  def set_end_date(self,enddate):
    self.enddate = enddate
  
  def get_employee_id(self):
    return self.employeeID

  def get_title(self):
    return self.title
  
  def get_forename(self):
    return self.forename
  
  def get_surname(self):
    return self.surname
  
  def get_email(self):
    return self.email
  
  def get_salary(self):
    return self.salary

  def get_start_date(self):
    return self.startdate
  
  def get_end_date(self):
    return self.enddate

  def __str__(self):
    return str(self.employeeID)+"\n"+self.title+"\n"\
           + self.forename+"\n"+self.surname+"\n"+self.email\
           +"\n"+str(self.salary)+"\n"+str(self.startdate)\
           +"\n"+str(self.enddate)
    