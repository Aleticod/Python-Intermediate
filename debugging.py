def divisors(num):
  divisors = []
  for i in range(1, num + 1):
    import pdb; pdb.set_trace()
    if num % i == 0:
      divisors.append(i)
  return divisors


def run():
  num = int(input("Ingrese un numero: "))
  print(divisors(num))
  print("Termino el programa")
  


if __name__ == '__main__':
  run()