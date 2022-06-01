def run():
  my_list = [1, "hello", True, 4.5]
  my_dict = {"firtname": "Facundo", "lastname": "Garcia"}

  super_list = [
    {"firtname": "Facundo", "lastname": "Garcia"},
    {"firtname": "Harvey", "lastname": "Pfoccori"},
    {"firtname": "Lissbeth", "lastname": "Huaman"},
    {"firtname": "Fernanda", "lastname": "Gariion"},
    {"firtname": "Daniela", "lastname": "Roman"},
  ]
  super_dic = {
    "natural-nums": [1, 2, 3, 4],
    "integer-nums": [-1, 2, -3, 4],
    "floating-nums": [-1.2, 2, -3, 4.5],
  }

  # this prints the values of super_dic
  for key, value in super_dic.items():
    print(key, "- ", value)

  # This block prints the value of super_list
  for values_list in super_list:
    print("Person data")
    for key, value in values_list.items():
      print("\t", key, "-", value)

  # This is other to printing a super_list
  for item in super_list:
    print(item["firtname"], " ", item["lastname"])


if __name__ == '__main__':
  run()
  