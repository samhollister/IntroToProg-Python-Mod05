# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   SHollister,5/21/25,Created Script
# ------------------------------------------------------------------------------------------ #

# Import libraries
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("File not found.")
    print("--Technical Error Documentation--")
    print(e, e.__doc__, type(e), sep = "\n")
except Exception as e:
    print("Unspecified error.")
    print("--Technical Error Documentation--")
    print(e, e.__doc__, type(e), sep = "\n")
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name should only contain letters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name should only contain letters.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
        except ValueError as e:
            print(e)
            print("--Technical Error Documentation--")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Unspecified error.")
            print("--Technical Error Documentation--")
            print(e, e.__doc__, type(e), sep = "\n")

        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            file.close()
            print("The following data was saved to file:")
            print("-"*50)
            for student in students:
                print(f"FirstName: {student["FirstName"]}, LastName: {student["LastName"]}, CourseName: {student["CourseName"]}")
            print("-"*50)
        except TypeError as e:
            print("Please check that the data is in a valid JSON format.")
            print("--Technical Error Documentation--")
            print(e, e.__doc__, type(e), sep = "\n")
        except Exception as e:
            print("Unspecified error.")
            print("--Technical Error Documentation--")
            print(e, e.__doc__, type(e), sep = "\n")
        finally:
            if file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
