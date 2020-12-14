import csv
full_roster = [] #Creating a list of lists to add to later on. 
totalPay = 0
class Person:
  jobTitle = ''
  wage = 0
  effort = 0

  def __init__(self, jobTitle, wage, effort):
      self.jobTitle = jobTitle
      self.wage = wage
      self.effort = effort

  def add_personnel(self): # A list for storing Personnel added to the job
      full_roster.append(self)
      print(self.jobTitle + " was added to the roster")
