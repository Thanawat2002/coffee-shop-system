import datetime
from utils import read_file

SALES_FILE = "sales.txt"

def report_daily_sales():
  sales = read_file(SALES_FILE)
  today = datetime.date.today()
  total_sales = 0

  for sale in sales:
    date = sale.split(",")[-1].split()[0]
    if date == str(today):
      total_sales += float(sale.split(",")[4])
  
  print("Sales separated by product:")

  products = {}
  for sale in sales:
    date = sale.split(",")[-1].split()[0]
    if date == str(today):
      product_name = sale.split(",")[2]
      price = float(sale.split(",")[4])
      if product_name in products:
        products[product_name] += price
      else:
        products[product_name] = price

  for product, price in products.items():
    print(f"{product}: {price} bath")

  print(f"Total sales for {today}: {total_sales} bath")

def report_sales_by_employee():
  sales = read_file(SALES_FILE)
  
  employees = {}
  for sale, employee in zip(sales, read_file("employees.txt")):
    employee_id = employee.split(",")[0]
    employee_name = employee.split(",")[1]
    if employee_id in employees:
      employees[employee_id]["sales"] += float(sale.split(",")[4])
    else:
      employees[employee_id] = {"name": employee_name, "sales": float(sale.split(",")[4])}

  for employee_id, data in employees.items():
    print(f"{data['name']} sold {data['sales']} bath")

def report_total_sales():
  sales = read_file(SALES_FILE)
  total_sales = sum([float(sale.split(",")[4]) for sale in sales])
  print(f"Total sales: {total_sales} bath")

def calculate_commission():
  sales = read_file(SALES_FILE)
  employees = read_file("employees.txt")
  
  employee_sales = {}
  for sale in sales:
    employee_id = sale.split(",")[0]
    price = float(sale.split(",")[4])
    if employee_id in employee_sales:
      employee_sales[employee_id] += price
    else:
      employee_sales[employee_id] = price

  for employee in employees:
    employee_id = employee.split(",")[0]
    employee_name = employee.split(",")[1]
    commission = float(employee.split(",")[2])
    if employee_id in employee_sales:
      total_sales = employee_sales[employee_id]
      total_commission = total_sales * commission / 100
      print(f"{employee_name} sold {total_sales} bath and earned {total_commission} bath in commission")
    else:
      print(f"{employee_name} sold 0 bath and earned 0 bath in commission")
