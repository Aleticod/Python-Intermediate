from functools import reduce

def run():
  
  # Filter function use
  my_list = [1, 4, 5, 6, 9, 13, 19, 21]
  print("This is the filter code")
  odd = list(filter(lambda x: x % 2 != 0, my_list))
  print(odd)

  # Map function use
  print("This is the map code")
  squares = list(map(lambda x: x ** 2, my_list))
  print(squares)

  # Reduce function use
  other_list = [2, 2, 2, 2, 2]
  print("This is the reduce code")
  reduced = reduce(lambda a, b: a * b, other_list)
  print(reduced)

if __name__ == '__main__':
  run()