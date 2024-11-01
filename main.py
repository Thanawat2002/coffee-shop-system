from employees import *
from products import *
from sales import *
from report import *

def main_menu():
  while True:
    print("\n==== Main Menu ====")
    print("1. Employees")
    print("2. Products")
    print("3. Sales")
    print("4. Reports")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      employees_menu()
    elif choice == '2':
      products_menu()
    elif choice == '3':
      sales_menu()
    elif choice == '4':
      reports_menu()
    elif choice == '0':
      break
    else:
      print("Invalid choice")

def employees_menu():
  while True:
    print("\n==== Employees Menu ====")
    print("1. Add employee")
    print("2. List employees")
    print("0. Back")

    choice = input("Enter your choice: ")

    if choice == '1':
      add_employee()
    elif choice == '2':
      list_employees()
    elif choice == '0':
      break
    else:
      print("Invalid choice")

def products_menu():
  while True:
    print("\n==== Products Menu ====")
    print("1. Add product")
    print("2. List products")
    print("0. Back")

    choice = input("Enter your choice: ")

    if choice == '1':
      add_product()
    elif choice == '2':
      list_products()
    elif choice == '0':
      break
    else:
      print("Invalid choice")

def sales_menu():
  while True:
    print("\n==== Sales Menu ====")
    print("1. Buy product")
    print("0. Back")

    choice = input("Enter your choice: ")

    if choice == '1':
      buy_product()
    elif choice == '0':
      break
    else:
      print("Invalid choice")

def reports_menu():
  while True:
    print("\n==== Reports Menu ====")
    print("1. Daily sales")
    print("2. Sales by employee")
    print("3. Total sales")
    print("4. Calculate Commission")
    print("0. Back")

    choice = input("Enter your choice: ")

    if choice == '1':
      report_daily_sales()
    elif choice == '2':
      report_sales_by_employee()
    elif choice == '3':
      report_total_sales()
    elif choice == '4':
      calculate_commission()
    elif choice == '0':
      break
    else:
      print("Invalid choice")

if __name__ == '__main__':
  main_menu()