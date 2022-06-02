from email.encoders import encode_7or8bit


def read():
  numbers = []
  with open("./files/numbers.txt","r",encoding="utf-8") as f:
    for line in f:
      numbers.append(int(line))
  print(numbers)

def write():
  names = ["facundo", "pepe", "miguel", "lian", "ana maria"]
  with open("./files/names.txt","a", encoding="utf-8") as f:
    for name in names:
      f.write(name)
      f.write("\n")
    f.close()



def run():
  read()
  write()


if __name__ == '__main__':
  run()