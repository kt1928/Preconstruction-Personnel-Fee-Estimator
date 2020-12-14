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

  def calc_hours(self,weeks,effort): # A list to calculate how many hours the personnel will work based on their effort precentage
      return weeks*40*(effort/100) # Assumed an average work week is 40  hours. Can be ajusted for more accurate estimation

  def calc_pay(self, wages,weeks,effort): # A list to calculate how much each personnel is payed 
      self.pay = self.calc_hours(weeks,effort) * wages # (hours worked * wage per hour)
      return self.calc_hours(weeks,effort) * wages

  def __str__(self):
      return "Title: " + self.jobTitle + ", Wage: " + str(self.wage) + ", Effort: " + str(self.effort)

  def write_to_csv(self, week, roster): # Exports inputted data as a csv
    with open('output.csv', mode='w') as roster_file:
        writer = csv.writer(roster_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for x in roster:
          writer.writerow([x.jobTitle, x.wage, x.effort, x.calc_pay(x.wage, week, x.effort)])
          
