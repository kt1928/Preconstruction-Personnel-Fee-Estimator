# Preconstruction-Personnel-Fee-Estimator
This program estimates preconstruction personnel fee for each phase of construction and the entire construction

Assumptions:

* A work week is 40 hours

Inputs:

* For each personnel, you will be asked to input their:
  * Job title
  * Wage per hour
  * Effort precentage 
  * Weeks worked

Output:

* A CSV containing each personnel's cost, the total cost estimate for the personnel for that phase of construction, and the total  

## Setup

Downlaod the program and unzip it. Then open the folder contaning the program in the enviroment of your choice. Make sure the csv file is in the same folder as the program

## How to use the program

Once the program is running, it will prompt the user to input the personnel's job title, wage per hour, effort percentage, and weeks worked. After each personnel is added, the program will continue to ask if the user is done. The user can either input 'exit' to move on to the phase or press return to continuing entering more inputs. After the user has inputted everything the program will export all entered information to a CSV for the user. 

This is the initial prompt: 

`What is the job title: `

`What is the job title: Precon Exec
Enter the wage, the effort precentage, and the amount of weeks it takes to complete the construction separated with a space:  `

An example entry should look like this: 50 23 45

This is how it will look after everything for that personnel is added.

`Current roster: 
What is the job title: Precon Exec
Enter the wage, the effort precentage, and the amount of weeks it takes to complete the construction separated with a space: 50 32 45
Entire Roster Pay: 28800.0
Precon Exec was added to the roster
Type 'exit' to exit the program or Press return to continue: `
