def run():
  pass
  # This is the definition of lambda function
  # This lambda function return if a word is palindromo
  palindromo = lambda string: string == string[::-1]
  if(palindromo('ana')):
    print("This word is a palindromo")
  else:
    print("This wors isn't palindromo")

if __name__ == '__main__':
  run()