def read_file(filename):
  try: 
    with open(filename, "r") as file:
      datas = file.readlines()
      for i in range(len(datas)):
        datas[i] = datas[i].strip()
    return datas
  except FileNotFoundError:
    return []