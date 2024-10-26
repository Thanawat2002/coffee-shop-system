from utils import read_file

EMPLOYEES_FILE = "employees.txt"

def read_employees():
  return read_file(EMPLOYEES_FILE)

def add_employee():
    employees = read_employees()
    if employees:
        last_id = int(employees[-1].split(",")[0])
        new_id = last_id + 1
    else:
        new_id = 1

    name = input("Enter employee name: ")
    commission = float(input("Enter commission: "))

    with open(EMPLOYEES_FILE, "a") as file:
        file.write(f'{new_id},{name},{commission}\n')
    
    print("Employee added successfully")

def list_employees():
    employees = read_employees()
    for emp in employees:
        print(emp)