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

  # for key, value in super_dic.items():
  #   print(key, "- ", value)

  for values_list in super_list:
    print("Person data")
    for key, value in values_list.items():
      print("\t", key, "-", value)


if __name__ == '__main__':
  run()
  