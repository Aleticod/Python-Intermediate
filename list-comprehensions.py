def run():
  squares = [] # definitio of empty list
  for i in range(1,101): # the last parameter is no inclusive
    # the i start in 1 and end in 100
    if(i % 3 != 0):
      squares.append(i ** 2)

  
  # print item of list
  for item in squares:
    print(item)

  # List comprehensions
  my_list = [i ** 2 for i in range (1, 101) if i % 3 != 0]

  print(my_list)

  ### RETO ###
  print()
  print("Desarrollo del reto de impirmr numero multiplos de 4, 6 y 9")
  other_list = [i for i in range (1, 1000) if (not(i % 4) and not(i % 6) and not(i % 9)) == 1]
  print(other_list)

if __name__ == '__main__':
  run() 