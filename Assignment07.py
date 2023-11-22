# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Jenna Ho,11/22/2023,Created Script
# ------------------------------------------------------------------------------------------ #
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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# TODO Create a Person Class
# TODO Add first_name and last_name properties to the constructor (Done)
# TODO Create a getter and setter for the first_name property (Done)
# TODO Create a getter and setter for the last_name property (Done)
# TODO Override the __str__() method to return Person data (Done)

# self. gives def to variable first name
class Person:
    """
    initiate the object:self, and parameters have first name and last name
    """
    def __init__(self, first_name, last_name):
        """
        validation code - throw the error that first name must be alphabetical
        """
        if first_name.isalpha():
            self.first_name = first_name
        else:
            raise ValueError("the first name should not contain numbers")
        if last_name.isalpha():
            self.last_name = last_name
        else:
            raise ValueError("the last name should not contain numbers")
    """
    getters is to get access to first name
    """
    def get_first_name(self):
        return self.first_name
    """
    getters is to get access to first name
    """
    def get_last_name(self):
        return self.last_name
    """
    setters allow you to change an attribute
    """
    def set_first_name(self,first_name):
        if first_name.isalpha():
            self.first_name = first_name
        else:
            raise ValueError("the first name should not contain numbers")

    """
    setters allow you to change an attribute
    """
    def set_last_name(self,last_name):
        if last_name.isalpha():
            self.last_name = last_name
        else:
            raise ValueError("the last name should not contain numbers")

    """
    return person's first name and last name
    """
    def __str__(self):
        return self.first_name + ' ' + self.last_name
# TODO Create a Student class the inherits from the Person class (Done)
# TODO call to the Person constructor and pass it the first_name and last_name data (Done)
# TODO add a assignment to the course_name property using the course_name parameter (Done)
# TODO add the getter for course_name (Done)
# TODO add the setter for course_name (Done)
# TODO Override the __str__() method to return the Student data (Done)
"""
student inherit everything from person
"""
class Student(Person):
    """
    initiate the object:self, and parameters have first name and last name. Super gives the person first name
    and last name
    """
    def __init__(self, first_name, last_name, course_name):
        super().__init__(first_name, last_name)
        self.course_name = course_name
    """
    getters is to get access to first name
    """
    def get_course_name(self):
        return self.course_name
    """
    setters allow you to change an attribute
    """
    def set_course_name(self,course_name):
        self.course_name = course_name
    """
    return calls the string method of person's first name and last name, and addes the course name
    """
    def __str__(self):
        return super().__str__() + ' is enrolled in ' + self.course_name


# Processing --------------------------------------- #
class FileProcessor:
    """
A collection of processing layer functions that work with Json files

ChangeLog: (Who, When, What)
RRoot,1.1.2030,Created Class
"""


    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")
            student_list = json.load(file)
            """
            define person object from JSON file
            """
            for student in student_list:
                person = Student(student["first_name"], student["last_name"], student["course_name"])
                student_data.append(person)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
            RRoot,1.1.2030,Created function

            :param file_name: string data with name of file to write to
            :param student_data: list of dictionary rows to be writen to the file

            :return: None
            """

        try:
            file = open(file_name, "w")
            """
            converts the student list into a format that JSON file can write to
            """
            student_list = [student.__dict__ for student in student_data]
            json.dump(student_list, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")

        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice


    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            """
            calls the str method of the student
            """
            print(student)
        print("-" * 50)


    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            course_name = input("Please enter the name of the course: ")
            student = Student(student_first_name, student_last_name, course_name)
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
                IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
                IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

