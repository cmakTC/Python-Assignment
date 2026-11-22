while True:
  try:
    value1, value2 = map(int, input("Give me two numbers: ").split())
  except ValueError:
    print("Error: Did not provide a value that can be casted to an int.")
    exit()
  op = input("Choose a mathmatical operation: ")
  if(op == "q"):
    exit()
  if(op == "+"):
    print(value1 + value2)
  elif(op == "-"):
    print(value2 - value1)
  elif(op == "*"):
    print(value1 * value2)
  elif(op == "%"):
    print(value1 % value2)
  elif(op == "**"):
    print(value1 ** value2)
  else:
    print("Error, invalid operation provided.")
