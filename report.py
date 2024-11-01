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
  
  # print("Sales separated by product:")

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

  # for product, price in products.items():
  #   print(f"{product}: {price} bath")

  # print(f"Total sales for {today}: {total_sales} bath")
  header_table = f"|{'No.':^10}|{'Product':^20}|{'Price':^10}|"
  data_table = []
  for i, (product, price) in enumerate(products.items(), 1):
    data_table.append([i,product,price])
  report_table(header_table, data_table, total_sales, today)

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

  # for employee_id, data in employees.items():
  #   print(f"{data['name']} sold {data['sales']} bath")
  header_table = f"|{'No.':^10}|{'Employee':^20}|{'Sales':^10}|"
  data_table = []
  for i, (employee_id, data) in enumerate(employees.items(), 1):
    data_table.append([i,data['name'],data['sales']])
  report_table(header_table, data_table)

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

  header_table = f"|{'No.':^10}|{'Employee':^20}|{'Commission':^10}|"
  data_table = []
  for i, employee in enumerate(employees, 1):
    employee_id = employee.split(",")[0]
    employee_name = employee.split(",")[1]
    commission = float(employee.split(",")[2])
    if employee_id in employee_sales:
      total_sales = employee_sales[employee_id]
      total_commission = total_sales * commission / 100
      data_table.append([i,employee_name,total_commission])
    else:
      data_table.append([i,employee_name,0])
  report_table(header_table, data_table)
  
def report_table(header, data, total_sales = None, today = None):
  separator = "=" * 44

  if today:
    print(f"\nTotal sales for {today}".center(len(separator)))
  print(separator)
  print(header)
  print(separator)
  for row in data:
    print(f"|{row[0]:^10}:{row[1]:^20}:{row[2]:^10}|")
  print(separator)
  if total_sales:
    print(f"Total sales: {total_sales} bath")