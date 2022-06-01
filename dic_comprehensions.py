from itertools import chain


def run():
  my_dictionary = {}

  for i in range(1, 101):
    if (i % 3 != 0):
      my_dictionary[i] = i ** 3
  
  print(my_dictionary)

  # Dictionary comprehensions
  print("This is the dictionary comprehensions")
  my_dic = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}
  print(my_dic)

  # This is the challenge
  print("this print the challenge")
  challenge = {i: i ** 0.5 for i in range (1, 101)}
  print(challenge)

# Entry point 
if __name__ == '__main__':
  run()