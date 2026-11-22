

def printOddNumbers():
  for i in range(1, 20):
    if i % 2 == 1:
      print(i)

def printFiftySevenTable():
  for i in range(1, 11):
    print(f"57 x {i} = {57 * i}")
    
def printMultiplesOfThreeFromOneToFifty():
  for i in range(1, 51):
    if i % 3 == 0:
      if i == 15:
        continue
      print(i)
      
def divisibleByTwoValues():
  val1, val2 = 0, 0
  while val1 < 0 or val2 < 0:
    try:
      val1 = int(input("Enter the first value: "))
      val2 = int(input("Enter the second value: "))
      if val1 < 0 or val2 < 0:
        print("Please enter positive integers only.")
    except ValueError:
      print("Invalid input. Please enter integers only.")
  val1 = int(input("Enter the first value: "))
  val2 = int(input("Enter the second value: "))
  for i in range(1, 1001):
    if i % val1 == 0 and i % val2 == 0:
      print(i)
      break
      
def main():
  choice = input("Choose an option (1-4):\n1. Print Odd numbers from 1 to 20\n2. Print the table of 57\n3. Print all the multiples of three from 1 to 50 but skip 15.\n4. Find the first number divisible by two provided values between 1 and 1000.\n")
  
  if choice == "1":
    printOddNumbers()
  elif choice == "2":
    printFiftySevenTable()
  elif choice == "3":
    printMultiplesOfThreeFromOneToFifty()
  elif choice == "4":
    divisibleByTwoValues()
  else:
    print("Invalid choice. Please select a number between 1 and 4.")