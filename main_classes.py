
# we're creating an employee class with basic attributes and are passing onboarding classe's object as a value to one of employees's attributes

from datetime import datetime






class Onboarding:
  """
  This class represents the onboarding program for a new employee.
  """
  def __init__(self, welcome_package, team_meetings, training_modules, mentor_details):
    """
    Initializes an Onboarding object with the details of the program.

    Args:
        welcome_package (str): Description of the welcome package provided to the new hire.
        team_meetings (list): List of planned team meetings during onboarding.
        training_modules (list): List of training modules the new hire will complete.
        mentor_details (str): Information about the assigned mentor.
    """
    self.welcome_package = welcome_package
    self.team_meetings = team_meetings
    self.training_modules = training_modules
    self.mentor_details = mentor_details

  def __str__(self):
    """
    Returns a string representation of the Onboarding object.

    Returns:
        str: A string summarizing the onboarding program details.
    """
    return f"Onboarding Program: Welcome Package: {self.welcome_package}, Team Meetings: {self.team_meetings}, Training Modules: {self.training_modules}, Mentor: {self.mentor_details}"


class Employee:
  """
  This class represents an employee in the organization.
  """
  def __init__(self, name, email, department, job_title, start_date, employee_id, onboarding_program):
    """
    Initializes an Employee object with the given attributes and an onboarding program object.

    Args:
        name (str): Employee's name.
        email (str): Employee's email address.
        department (str): Employee's department.
        job_title (str): Employee's job title.
        start_date (str): Employee's start date.
        employee_id (str): Unique employee identifier.
        onboarding_program (Onboarding): An Onboarding object representing the employee's onboarding program.
    """
    self.name = name
    self.email = email
    self.department = department
    self.job_title = job_title
    self.start_date = start_date
    self.employee_id = employee_id
    self.onboarding_program = onboarding_program

    for parameter in parameters:
      setattr(self, parameter, None)

  def __str__(self):
    """
    Returns a string representation of the Employee object with onboarding details.

    Returns:
        str: A string representation of the employee information including onboarding program details.
    """
    return f"Employee: {self.name} - Email: {self.email} - Department: {self.department} \nOnboarding Program: {self.onboarding_program}"



all_employees = []





parameters=[]


def add_parameters():
  para=input("enter parameter")
  parameters.append(para)

name=input("enter name") 
email=input("enter email") 
dept=input("enter dept")
title=input("enter title")
st = datetime.strptime(input("Enter start date (dd/mm/yyyy): "), "%d/%m/%Y")
emp_id=input("enetr employee id")


welcome_package_str = input("Enter welcome package items separated by commas (e.g., laptop, mug, etc.): ")
welcome_package_list = welcome_package_str.split(",")

welcome_package_list = [item.strip() for item in welcome_package_list]


team_meetings_str = input("Enter planned team meetings separated by commas (e.g., Sales Kickoff, Engineering Team Meeting): ")
team_meetings_list = team_meetings_str.split(",")
team_meetings_list = [meeting.strip() for meeting in team_meetings_list]

training_modules_str = input("Enter training modules separated by commas (e.g., Company Policies, Sales Techniques): ")
training_modules_list = training_modules_str.split(",")
training_modules_list = [module.strip() for module in training_modules_list]

mentor_details=input("enter id of mentor")


onboarding_program = Onboarding(
  welcome_package_list,  
  team_meetings_list,
  training_modules_list,
  mentor_details
)



employee=Employee(name,email,dept,title,st,emp_id,onboarding_program,parameters)

all_employees.append(employee)



