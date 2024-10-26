import datetime
from utils import read_file
from employees import read_employees
from products import read_products


SALES_FILE = "sales.txt"

def buy_product():
  employees_data = read_employees()
  products_data = read_products()

  employee_id = input("Enter employee id: ")
  product_id = input("Enter product id: ")
  quantity = int(input("Enter quantity: "))

  employee = None
  product = None
  for emp, prod in zip(employees_data, products_data):
    if emp.split(",")[0] == employee_id:
      employee = emp
    if prod.split(",")[0] == product_id:
      product = prod

  if employee is None:
    print("Employee not found")
    return

  if product is None:
    print("Product not found")
    return

  employee_name = employee.split(",")[1]

  product_name = product.split(",")[1]
  price = float(product.split(",")[2])

  total_price = price * quantity
  date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  with open(SALES_FILE, "a") as file:
    file.write(f"{employee_id},{product_id},{product_name},{quantity},{total_price},{date_time}\n")
  print(f"{employee_name} sold {quantity} {product_name} for {total_price} bath at {date_time}")
