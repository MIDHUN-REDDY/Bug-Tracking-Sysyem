Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="Your_username",
        password="Your_password",
        database="bds",
        charset="utf8"
    )

def main_menu():
    while True:
        print("\n******* MAIN MENU ********")
        print("1. ADMIN MODULE")
        print("2. MANAGER PANEL")
        print("3. EMPLOYEE PANEL")
        print("4. EXIT")
        choice = int(input("Enter the number to open module: "))
        if choice == 1:
            admin_module()
        elif choice == 2:
            manager_panel()
        elif choice == 3:
            employee_panel()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE! Please try again.")

def admin_module():
    while True:
        print("\n****** ADMIN MODULE *******")
        print("1. MANAGER")
        print("2. EMPLOYEE")
        print("3. VIEW ALL PROJECTS")
        print("4. VIEW BUG REPORTS")
        print("5. EXIT")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            admin_module_manager()
        elif choice == 2:
            admin_module_employee()
        elif choice == 3:
            admin_module_view_all_projects()
        elif choice == 4:
            view_all_bugs()
        elif choice == 5:
            print("Returning to Main Menu...")
            break
        else:
            print("INVALID CHOICE! Please try again.")

def admin_module_manager():
    while True:
        print("\n******* MANAGER *******")
        print("1. ADD MANAGER ACCOUNT")
        print("2. VIEW MANAGER ACCOUNT")
        print("3. DELETE MANAGER")
        print("4. UPDATE MANAGER DETAILS")
        print("5. RETURN TO ADMIN MODULE")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_manager_account()
        elif choice == 2:
            view_manager_account()
        elif choice == 3:
            delete_manager()
        elif choice == 4:
            update_manager_details()
        elif choice == 5:
            break
        else:
            print("INVALID CHOICE! Please try again.")

def add_manager_account():
    print("\n******* ADDING MANAGER DETAILS *******")
    try:
        empcode = int(input("Enter Employee Code: "))
        empname = input("Enter Name: ").strip()
        if not empname:
            print("Name cannot be empty.")
            return
        empemail = input("Enter Email: ").strip()
        if '@' not in empemail or not empemail:
            print("Please enter a valid email address.")
            return
        emppassword = input("Enter Password: ").strip()
        if len(emppassword) < 8:
            print("Password must be at least 8 characters long.")
            return
        gender = input("Enter Gender ('M' or 'F'): ").strip().upper()
        if gender not in ['M', 'F']:
            print("Invalid gender. Please enter 'M' or 'F'.")
            return
        dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
        mobileno = input("Enter Mobile Number: ").strip()
        if not mobileno.isdigit() or len(mobileno) != 10:
            print("Please enter a valid 10-digit mobile number.")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO employee (empcode, empname, empemail, emppassword, gender, dob, mobileno, role)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, 'Manager')"""
        cursor.execute(query, (empcode, empname, empemail, emppassword, gender, dob, mobileno))
        conn.commit()
        print("Manager added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def view_manager_account():
    print("\n****** VIEW MANAGER'S ACCOUNT *******")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee WHERE role='Manager'")
    managers = cursor.fetchall()
    if not managers:
        print("No managers found.")
    else:
        for row in managers:
            print(row)
    cursor.close()
    conn.close()

def delete_manager():
    empcode = int(input("Enter Employee Code of the manager to delete: "))
    conn = get_db_connection()
    cursor = conn.cursor()
...     query = "DELETE FROM employee WHERE empcode = %s AND role = 'Manager'"
...     cursor.execute(query, (empcode,))
...     conn.commit()
...     if cursor.rowcount > 0:
...         print("Manager deleted successfully.")
...     else:
...         print("Manager not found.")
...     cursor.close()
...     conn.close()
... 
... def update_manager_details():
...     print("\n****** UPDATE MANAGER DETAILS ******")
...     empcode = int(input("Enter Employee Code of the manager to update: "))
...     new_name = input("Enter New Name: ").strip()
...     new_email = input("Enter New Email: ").strip()
...     new_password = input("Enter New Password: ").strip()
...     new_gender = input("Enter New Gender (M/F): ").strip().upper()
...     new_dob = input("Enter New Date of Birth (YYYY-MM-DD): ").strip()
...     new_mobile_no = input("Enter New Mobile Number: ").strip()
...     conn = get_db_connection()
...     cursor = conn.cursor()
...     query = """UPDATE employee SET empname = %s, empemail = %s, emppassword = %s, gender = %s, dob = %s, mobileno = %s 
...                WHERE empcode = %s AND role = 'Manager'"""
...     cursor.execute(query, (new_name, new_email, new_password, new_gender, new_dob, new_mobile_no, empcode))
...     conn.commit()
...     if cursor.rowcount > 0:
...         print("Manager details updated successfully.")
...     else:
...         print("Manager not found.")
...     cursor.close()
...     conn.close()
... 
... # Employee Module
... def admin_module_employee():
...     while True:
...         print("\n****** EMPLOYEE *******")
...         print("1. ADD EMPLOYEE ACCOUNT")
...         print("2. VIEW EMPLOYEE ACCOUNTS")
...         print("3. DELETE EMPLOYEE ACCOUNT")
...         print("4. UPDATE EMPLOYEE DETAILS")
...         print("5. RETURN TO ADMIN MODULE")
...         choice = int(input("Enter your choice: "))
...         if choice == 1:
...             add_employee_account()
...         elif choice == 2:
            view_employee_account()
        elif choice == 3:
            delete_employee_account()
        elif choice == 4:
            update_employee_details()
        elif choice == 5:
            break
        else:
            print("INVALID CHOICE! Please try again.")

def add_employee_account():
    print("\n********* ADD EMPLOYEE ACCOUNT *********")
    try:
        empcode = int(input("Enter Employee Code: "))
        empname = input("Enter Name: ").strip()
        if not empname:
            print("Name cannot be empty.")
            return
        empemail = input("Enter Email: ").strip()
        if '@' not in empemail or not empemail:
            print("Please enter a valid email address.")
            return
        emppassword = input("Enter Password: ").strip()
        if len(emppassword) < 8:
            print("Password must be at least 8 characters long.")
            return
        gender = input("Enter Gender (M/F): ").strip().upper()
        if gender not in ['M', 'F']:
            print("Invalid gender. Please enter 'M' or 'F'.")
            return
        dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
        mobileno = input("Enter Mobile Number: ").strip()
        if not mobileno.isdigit() or len(mobileno) != 10:
            print("Please enter a valid 10-digit mobile number.")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO employee (empcode, empname, empemail, emppassword, gender, dob, mobileno, role)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, 'Employee')"""
        cursor.execute(query, (empcode, empname, empemail, emppassword, gender, dob, mobileno))
        conn.commit()
        print("Employee added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def view_employee_account():
    print("\n******** VIEW EMPLOYEE ACCOUNTS ********")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee WHERE role='Employee'")
    employees = cursor.fetchall()
    if not employees:
        print("No employees found.")
    else:
        for row in employees:
            print(row)
    cursor.close()
    conn.close()

def delete_employee_account():
    empcode = int(input("Enter Employee Code of the employee to delete: "))
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM employee WHERE empcode = %s AND role = 'Employee'"
    cursor.execute(query, (empcode,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")
    cursor.close()
    conn.close()

def update_employee_details():
    print("\n****** UPDATE EMPLOYEE DETAILS ******")
    empcode = int(input("Enter Employee Code of the employee to update: "))
    new_name = input("Enter New Name: ").strip()
    new_email = input("Enter New Email: ").strip()
    new_password = input("Enter New Password: ").strip()
    new_gender = input("Enter New Gender (M/F): ").strip().upper()
    new_dob = input("Enter New Date of Birth (YYYY-MM-DD): ").strip()
    new_mobile_no = input("Enter New Mobile Number: ").strip()
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """UPDATE employee SET empname = %s, empemail = %s, emppassword = %s, gender = %s, dob = %s, mobileno = %s 
               WHERE empcode = %s AND role = 'Employee'"""
    cursor.execute(query, (new_name, new_email, new_password, new_gender, new_dob, new_mobile_no, empcode))
    conn.commit()
    if cursor.rowcount > 0:
        print("Employee details updated successfully.")
    else:
        print("Employee not found.")
    cursor.close()
    conn.close()

# Manager Panel
def manager_panel():
    while True:
        print("\n****** MANAGER PANEL ******")
        print("1. VIEW PROJECTS")
        print("2. ASSIGN TASKS")
        print("3. VIEW BUG REPORTS")
        print("4. UPDATE BUG STATUS")
        print("5. RETURN TO MAIN MENU")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_projects_manager_panel()
        elif choice == 2:
            assign_tasks_manager_panel()
        elif choice == 3:
            view_bug_reports_manager_panel()
        elif choice == 4:
            update_bug_status_manager_panel()
        elif choice == 5:
            break
        else:
            print("INVALID CHOICE! Please try again.")

def view_projects_manager_panel():
    print("\n****** VIEW PROJECTS ******")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    if not projects:
        print("No projects found.")
    else:
        for row in projects:
            print(row)
    cursor.close()
    conn.close()

def assign_tasks_manager_panel():
    print("\n****** ASSIGN TASKS ******")
    try:
        taskid = int(input("Enter Task ID: "))
        projectid = int(input("Enter Project ID: "))
        empcode = int(input("Enter Employee Code: "))
        taskdesc = input("Enter Task Description: ").strip()
        deadline = input("Enter Deadline (YYYY-MM-DD): ").strip()
        status = input("Enter Task Status: ").strip()

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO tasks (taskid, projectid, empcode, taskdesc, deadline, status)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (taskid, projectid, empcode, taskdesc, deadline, status))
        conn.commit()
        print("Task assigned successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def view_bug_reports_manager_panel():
    print("\n****** VIEW BUG REPORTS ******")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bugreport")
    bugs = cursor.fetchall()
    if not bugs:
        print("No bug reports found.")
    else:
        for row in bugs:
            print(row)
    cursor.close()
    conn.close()

def update_bug_status_manager_panel():
    print("\n****** UPDATE BUG STATUS ******")
    bugno = int(input("Enter Bug Number: "))
    new_status = input("Enter New Status: ").strip()
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE bugreport SET status = %s WHERE bugno = %s"
    cursor.execute(query, (new_status, bugno))
    conn.commit()
    if cursor.rowcount > 0:
        print("Bug status updated successfully.")
    else:
        print("Bug report not found.")
    cursor.close()
    conn.close()

# Employee Panel
def employee_panel():
    while True:
        print("\n****** EMPLOYEE PANEL ******")
        print("1. VIEW ASSIGNED TASKS")
        print("2. VIEW BUGS")
        print("3. UPDATE BUG STATUS")
        print("4. RETURN TO MAIN MENU")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_assigned_tasks_employee_panel()
        elif choice == 2:
            view_bugs_employee_panel()
        elif choice == 3:
            update_bug_status_employee_panel()
        elif choice == 4:
            break
        else:
            print("INVALID CHOICE! Please try again.")

def view_assigned_tasks_employee_panel():
    print("\n****** VIEW ASSIGNED TASKS ******")
    empcode = int(input("Enter Your Employee Code: "))
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM tasks WHERE empcode = %s"
    cursor.execute(query, (empcode,))
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks assigned.")
    else:
        for row in tasks:
            print(row)
    cursor.close()
    conn.close()

def view_bugs_employee_panel():
    print("\n****** VIEW BUGS ******")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bugreport")
    bugs = cursor.fetchall()
    if not bugs:
        print("No bugs found.")
    else:
        for row in bugs:
            print(row)
    cursor.close()
    conn.close()

def update_bug_status_employee_panel():
    print("\n****** UPDATE BUG STATUS ******")
    bugno = int(input("Enter Bug Number: "))
    new_status = input("Enter New Status: ").strip()
    new_bugdesc = input("Enter New Bug Description: ").strip()
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE bugreport SET status = %s, bugdes = %s WHERE bugno = %s"
    cursor.execute(query, (new_status, new_bugdesc, bugno))
    conn.commit()
    if cursor.rowcount > 0:
        print("Bug status updated successfully.")
    else:
        print("Bug report not found.")
    cursor.close()
    conn.close()

def view_all_bugs():
    print("\n****** VIEW ALL BUG REPORTS ******")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bugreport")
    bugs = cursor.fetchall()
    if not bugs:
        print("No bug reports found.")
    else:
        for row in bugs:
            print(row)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main_menu()
