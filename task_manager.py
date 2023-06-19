'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
with open('user.txt', 'r') as user:
    for line in user:
        # Split the password and username from the text file and remove any white space
        login_details = [word.strip() for word in line.strip().split(",")]

        # Save the username and password into two different variables
        username = login_details[0]
        password = login_details[1]

# Ask the user to enter their username and password 
login_username = input("Please enter your username: ")
login_password = input("Please enter your password: ")

# If the username and password match the ones in 'user.txt' print the code below and present the menu
if username == login_username and password == login_password:
    print("Login successful")
# If the username and or password do not match the ones in 'user.txt' the code below will print until the right credentials are entered
else:
    print("Incorrect username or password. Please try again!")
    login_username = input("Please enter your username: ")
    login_password = input("Please enter your password: ")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if login_username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - Statistics
gr - Generate reports
e - Exit
: ''').lower()
    else: 
        menu = input('''Select one of the following options below:
        a - Adding a task
        va - View all tasks
        vm - View all my tasks
        e - exit''').lower()

    if menu == 'r' and login_username == 'admin':
        # Define a function called "reg_user()"
        def reg_user():
            pass
            '''In this block you will write code to add a new user to the user.txt file
            - You can follow the following steps:
                - Request input of a new username
                - Request input of a new password
                - Request input of password confirmation.
                - Check if the new password and confirmed password are the same.
                - If they are the same, add them to the user.txt file,
                - Otherwise you present a relevant message.'''
            
            while True:
                # Ask the user to enter a new username
                # Ask the user to enter a new password and confirm it by entering the password again
                new_username = input("Please enter the username you want to register: ")
                # Use an "if" loop to make sure that new_username != username
                if new_username == username:
                    # if new_username == username the code below will print
                    print("Username already exists. Please try registering with another username.")
                    # The user is sent back to the menu to pick another menu item
                    break
                new_password = input("Please enter a new password: ")
                confirm_new_password = input("Please confirm the password that you have entered above: ")

                # If the two passwords match, the code below will print
                if confirm_new_password == new_password:
                    # If the passwords match save the new credentials to 'user.txt'
                    with open('user.txt', 'a') as user:
                        user.write(new_username + " , " + confirm_new_password)
                    print("Username and password have been saved. Please login again")
                    break
                
                # If the two passwords do not match the code below will print
                else:
                    print("Passwords do not match. Please restart the program")
                    break
        # Print the function "reg_user()"
        print(reg_user())
        

    elif menu == 'a':
        def add_task():
            pass
            '''In this block you will put code that will allow a user to add a new task to task.txt file
            - You can follow these steps:
                - Prompt a user for the following: 
                    - A username of the person whom the task is assigned to,
                    - A title of a task,
                    - A description of the task and 
                    - the due date of the task.
                - Then get the current date.
                - Add the data to the file task.txt and
                - You must remember to include the 'No' to indicate if the task is complete.'''
            
            # Ask the user to answer certain questions in order to assign a task
            while True:
                username_assigned = input("Please enter the username that has been assigned this task: ")
                task_title = input("Please enter the title of the task: ")
                task_description = input("Please describe the task: ")
                task_due_date = input("What is the due date for this task?: ")
                current_date = input("Please enter today's date: ")
                task_complete = input("Is the task currently complete? Yes or No ONLY: ")

                # Add a new task and write the task details into 'task.txt' 
                with open('tasks.txt', 'a') as tasks:
                    tasks.write("\n" + username_assigned + " , " + task_title + " , " + task_description + " , " + task_due_date + " , " + current_date + " , " + task_complete)
                    print("Task added to 'tasks.txt' ")
                    break
        # Print the function "add_task()"
        print(add_task())

    elif menu == 'va':
        def view_all():
            pass
            '''In this block you will put code so that the program will read the task from task.txt file and
            print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
            You can do it in this way:
                - Read a line from the file.
                - Split that line where there is comma and space.
                - Then print the results in the format shown in the Output 2 in L1T19 pdf
                - It is much easier to read a file using a for loop.'''

            # Open 'tasks.txt' as a read only file
            with open("tasks.txt", "r") as tasks:
                # Use a for loop to iterate over each line in 'tasks.txt' 
                for task in tasks:
                    # Strip each word and assign it to a variable 
                    task_details = [word.strip() for word in task.strip().split(",")]
                    user_assigned = task_details[0]
                    task_title2 = task_details[1]
                    task_description2 = task_details[2] 
                    task_due_date2 = task_details[3]
                    current_date2 = task_details[4]
                    task_complete2 = task_details[5]

                    # Print the tasks according to the template requested 
                    print("_______________________________________")
                    print("\n")
                    print("Task title: " + "\t" + task_title2)
                    print("Assigned to: " + "\t" + user_assigned)
                    print("Date assigned: " + "\t" + current_date2)
                    print("Due date: " + "\t" + task_due_date2)
                    print("Task complete?: " + "\t" + task_complete2)
                    print("Task description: " + "\t" + task_description2)
                    print("\n")
                    print("_________________________________________")
                    print("\n")
        # Print the function "view_all()"
        print(view_all())


    elif menu == 'vm':
        # define a function called "view_mine()"
        def view_mine():
            pass
            '''In this block you will put code the that will read the task from task.txt file and
            print to the console in the format of Output 2 presented in the L1T19 pdf
            You can do it in this way:
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the username you have
                read from the file.
                - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
            
            # Create a variable that can be used to keep count of the tasks
            task_number = 1

            # Open 'tasks.txt' as a read only file
            with open("tasks.txt", "r") as tasks:
                # Use a for loop to iterate over each line in 'tasks.txt' 
                for task in tasks:
                    # Strip each word and assign it to a variable 
                    task_details = [word.strip() for word in task.strip().split(",")]
                    user_assigned = task_details[0]
                    task_title2 = task_details[1]
                    task_description2 = task_details[2] 
                    task_due_date2 = task_details[3]
                    current_date2 = task_details[4]
                    task_complete2 = task_details[5]
                    task_number +=1

                    if login_username == user_assigned:                    
                        # Print the tasks according to the template requested
                        print("Task No: " + str(task_number)) 
                        print("_______________________________________")
                        print("\n")
                        print("Task title: " + "\t" + task_title2)
                        print("Assigned to: " + "\t" + user_assigned)
                        print("Date assigned: " + "\t" + current_date2)
                        print("Due date: " + "\t" + task_due_date2)
                        print("Task complete?: " + "\t" + task_complete2)
                        print("Task description: " + "\t" + task_description2)
                        print("\n")
                        print("_________________________________________")
                        print("\n")

                while True:
                    select_task = input("Please enter the number of the task you want to see. Otherwise select " + str(-1) + " to get back to the menu: ")

                    if select_task == "-1":
                        if login_username == "admin":
                            menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - Statistics
e - Exit
: ''').lower()
                        else:
                            menu = input('''Select one of the following options below:
                            a - Adding a task
                            va - View all tasks
                            vm - View my tasks
                            e - exit''').lower()
                    
                    else:
                        sub_menu = input("""Select to mark the test complete or to edit it:
                        E - Edit the task
                        C - Mark as complete""").lower()
                        
                        if sub_menu == "e":
                            edit_num = int(input("Enter the number of the task you want to edit"))
                            if edit_num == task_number:
                                print("Task No: " + str(task_number)) 
                                print("_______________________________________")
                                print("\n")
                                print("Task title: " + "\t" + task_title2)
                                print("Assigned to: " + "\t" + user_assigned)
                                print("Date assigned: " + "\t" + current_date2)
                                print("Due date: " + "\t" + task_due_date2)
                                print("Task complete?: " + "\t" + task_complete2)
                                print("Task description: " + "\t" + task_description2)
                                print("\n")
                                print("_________________________________________")
                                print("\n")

                            title = input("Enter the title of the task:\n")
                            description =input("describe the task:\n")
                            due_date = input("Enter the task due date dd/mm/yyyy:\n")
                            today_date = datetime.date.today()
                            completion = input("Is the tasks completed enter yes or no")
                            with open('tasks.txt','a+')as file:
                                file.writelines("\n")
                                file.writelines(f'''{username}, {title}, {description}, {due_date}, {today_date}, {completion}
                                            ''')
                                return "Date edited"
                            
                        elif sub_menu == 'C':
                            with open('tasks.txt','a') as file:
                                conte = " "
                                for line in file:
                                    conte = line.split(", ")
                                    if line.find(username) == 1:
                                        completion = 'yes'
                                        file.writelines(f'{completion}')
                            print("The task is marked as complete")     

                             
        # Print the function view_mine()
        print(view_mine())

    # create an if statetement for when the admin wants to see the statistics 
    elif menu == "s" and login_username == 'admin':
        
        # Create a a counter to add the number of usernames to
        count = 0 

        with open("user.txt", "r") as user:
                for line in user:
                    # Split the password and username from the text file and remove any white space
                    login_details = [word.strip() for word in line.strip().split(",")]

                    # Check if the line has a username and a password. If it does count it as a username
                    if len(login_details)== 2:
                        count += 1

        print("The number of usernames is: " + str(count))

        # Create a counter to add the number of tasks to
        count_tasks = 0

        with open("tasks.txt", "r") as tasks:
            for task in tasks:
                # Split the password and username from the text file and remove any white space
                task_details = [word.strip() for word in task.strip().split(",")]

                # Check if all six fields have been filled it to be avle to be counted as one task
                if len(task_details) == 6:
                    count_tasks += 1
        print("\n The amount of tasks is: " + str(count_tasks)+ "\n")

    elif menu == "gr" and login_username == "admin":

        #user overview function 
        def get_report():
            user_list = []
            tasks_list = []
            with open('user.txt','r+') as user_file:
                content = " "
                content = user_file.readlines()
                for line in content:
                    strip_cont = line.strip().split(", ")
                    user_list.append(strip_cont[0]) # storing users
                    
        # checking the tasks that are assigned per user and calculate they stats
        # creat the useroverview file and write the stats
            select_user = input("Select a username for statistics:\n")
            if select_user in user_list:
                completed_tasks = 0
                uncompleted_task = 0
                over_due = 0
                total_num_tasks = 0
            with open('tasks.txt','r') as tasks_file:
                lines = tasks_file.readlines()
                for line in lines:
                    total_num_tasks +=1
                    strip_cont = line.strip().split(", ")
                    tasks_list.append(strip_cont[1]) # add all the the tasks titles to tasks list, to find the total number of tasks.
                    if strip_cont[0] == select_user:
                        if strip_cont[-1] == 'yes':
                            completed_tasks += 1
                        elif strip_cont[-1] == 'no':
                            uncompleted_task += 1
                        elif strip_cont[-1]== 'no' and datetime.strftime("%m/%d/%Y") > datetime.today():
                            over_due += 1
                            
        # calculate the percentages                    
            total_num_tasks_gen = len(tasks_list)
            per_total_tasks = (total_num_tasks / len(tasks_list)) * 100
            per_completed_tasks = (completed_tasks / total_num_tasks) * 100
            per_uncompleted_tasks = (uncompleted_task / total_num_tasks) *100
            per_over_due_tasks = (over_due/total_num_tasks) * 100
            with open("useroverview.txt",'wt') as file:
                file.writelines(f"The total number of tasks is: {total_num_tasks}")
                file.writelines(f"\nThe number of completed tasks is : {completed_tasks}")
                file.writelines(f"\nThe number of uncompletestask is: {uncompleted_task}")
                file.writelines(f"\nThe number of overdue_tasks is: {over_due}\n")
                file.writelines(f"\nThe total perentange of the tasks assigned to the user is: {per_total_tasks}")
                file.writelines(f'\nThe percatange of completed tasks is: {per_completed_tasks}')
                file.writelines(f"\nThe percentage of uncompleted tasks is: {per_uncompleted_tasks}")
                file.writelines(f"\nThe percentage of over due tasks: {per_over_due_tasks}")
            print("Reports have been generated")
        print(get_report())

        # generate reports and create an task overviewfile
        # initiate all the wanted attribute and write them on the tasks overview file
        def get_report1():
            with open("tasks.txt","rt") as file:
                tasks_list = []
                uncompleted_tasks = 0
                completed_tasks = 0
                over_due_tasks = 0
                total_uncomp_over_due = 0
                content = " "
                content = file.readlines()
                for line in content:
                    lines = line.strip().split(", ")
                    tasks_list.append(lines[0])
                    if lines[-1] == "yes":
                        completed_tasks += 1
                    elif lines[-1] == "no":
                        uncompleted_tasks +=1
                    elif lines[-1]== 'no' and datetime.strftime("%m/%d/%Y") > datetime.today():
                        over_due_tasks += 1

            with open('tasks_overview.txt', 'wt') as file:
                total_num_tasks_gen = len(tasks_list)
                total_uncomp_over_due = over_due_tasks + uncompleted_tasks
                per_incomplete = (uncompleted_tasks / total_num_tasks_gen) * 100
                per_over_due_tasks = (over_due_tasks / total_num_tasks_gen) * 100
                file.writelines(f"The total number of generated tasks is: {total_num_tasks_gen}")
                file.writelines(f"\nThe total number of uncompleted tasks is: {uncompleted_tasks}")
                file.writelines(f"\nThe total number of over due tasks is: {over_due_tasks}")
                file.writelines(f"\nThe total number of completed tasks is: {completed_tasks}")
                file.writelines(f"\nThe total number of incomplete and over due tasks tasks is: {total_uncomp_over_due}")
                file.writelines(f"\nThe percentage of incomplete tasks is: {per_incomplete}")
                file.writelines(f"\nThe percentage of overfue tasks is: {per_over_due_tasks}")
        print(get_report1())
                
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")