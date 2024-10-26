from utils import read_file

PRODUCTS_FILE = "products.txt"

def read_products():
  return read_file(PRODUCTS_FILE)

def add_product():
  try:
    with open(PRODUCTS_FILE, "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            last_id = int(last_line.split(",")[0]) 
            new_id = last_id + 1
        else:
            new_id = 1  
  except FileNotFoundError:
    new_id = 1 

  name = input("Enter product name: ")
  price = float(input("Enter price: "))

  with open(PRODUCTS_FILE, "a") as file:
    file.write(f'{new_id},{name},{price}\n')
  print("Product added successfully")

def list_products():
  products = read_products()
  for prod in products:
    print(prod)