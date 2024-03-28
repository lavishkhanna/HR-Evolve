
# we're creating an employee class with basic attributes and are passing onboarding classe's object as a value to one of employees's attributes

from datetime import datetime
import streamlit as st


# Create empty dictionaries to store employee and onboarding data



def run():
    

  employees = {}
  onboarding_details = {}


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
          return (
              f"Onboarding Program: Welcome Package: {self.welcome_package}, "
              f"Team Meetings: {self.team_meetings}, "
              f"Training Modules: {self.training_modules}, "
              f"Mentor: {self.mentor_details}"
          )


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


  def add_employee_form():
      """Displays a form to collect employee information."""
      with st.form("Add Employee"):
          name = st.text_input("Name")
          email = st.text_input("Email")
          department = st.selectbox("Department", ["Marketing", "Engineering", "Sales"])
          job_title = st.text_input("Job Title")
          start_date = st.date_input("Start Date")
          employee_id = st.text_input("Employee ID (Optional)")
          onboarding_program = st.checkbox("Onboarding Program")
          submitted = st.form_submit_button("Add Employee")

          if submitted:
              # Generate an employee ID if not provided
              if not employee_id:
                  employee_id = f"EMP-{len(employees) + 1:04}"

              employees[employee_id] = Employee(
                  name,
                  email,
                  department,
                  job_title,
                  start_date,
                  employee_id,
                  None if not onboarding_program else Onboarding([], [], [], ""),
              )

              st.success(f"Employee '{name}' added successfully!")

  def add_onboarding_details_form(employee_id):
      """Displays a form to collect onboarding details for a specific employee."""
      if employee_id in employees:
          employee = employees[employee_id]
          with st.form(f"Onboarding Details for {employee.name}"):
              welcome_package = st.multiselect("Welcome Package", ["Laptop", "Desk Accessories", "Company Swag"])  # Use multiselect for lists
              team_meetings = st.text_input("Team Meetings (comma-separated)")
              training_modules = st.multiselect("Training Modules", ["Software Training", "Company Policies", "Safety Training"])
              mentor_details = st.text_input("Mentor Details")
              submitted = st.form_submit_button("Submit Onboarding Details")

              if submitted:
                  # Update onboarding program details for the employee
                  employee.onboarding_program = Onboarding(
                      welcome_package,
                      team_meetings.split(","),  # Split comma-separated string
                      training_modules,
                      mentor_details,
                  )
                  st.success(f"Onboarding details for '{employee.name}' submitted!")




  st.sidebar.title("Employee Management")
  add_employee_button = st.sidebar.button("Add Employee")
  if add_employee_button:
      add_employee_form()

  if employees:  # Only show onboarding form if there are employees
      selected_employee = st.selectbox("Select Employee for Onboarding Details", list(employees.keys()))
      add_onboarding_details_form(selected_employee)

  # Display existing employee data (optional)
  if employees:
      st.header("Employees")
      st.dataframe(employees.values())  # Display employee data in a table
  print(employees)
