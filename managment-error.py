def divisors(num):
  try:
    if(num < 0):
      raise ValueError("Ingrese un valor mayor a cero")
    divisors = []
    for i in range(1, num + 1):
      if num % i == 0:
        divisors.append(i)
    return divisors
  except ValueError as ve:
    print(ve)


# def run():
#   try:
#     num = int(input("Ingrese un numero: "))
#     print(divisors(num))
#     print("Termino el programa")
#   except ValueError:
#     print("Debes ingresar un numero")

def run():
  
  try:
    num = int(input("Ingrese un numeor: "))
    print(divisors(num))
    print("Termino el programa")
  except ValueError:
    print("Debes ingresar un numero")


if __name__ == '__main__':
  run()