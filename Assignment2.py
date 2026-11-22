import keyword;

def typeConversion():
  value = int(input("Enter an integer: "))
  text = input("Enter another number: ")
  print("The sum of the two numbers is:", value + int(text))
  return value + int(text)
  
  
def sumProgram():
  count = int(input("Enter how many numbers you want to add: "))
  total = 0
  for _ in range(count):
    total += int(input("Enter a number: "))
  print("The sum of the numbers is:", total)
  return total

def stringPractice():
  text = input("Enter a string: ")
  print("The string in uppercase is:", text.upper())
  print("The total number of characters in the string is:", len(text))
  vowelCount = 0
  for char in text:
      if char.lower() in 'aeiou':
        vowelCount += 1
  print("The total number of vowels in the string is:", vowelCount)
  return text
  
def checkKeyword():
  text = input("Enter a string to check: ")
  if keyword.iskeyword(text):
    print("Python keyword")
  else:
    print("Not a keyword")

def main():
  typeConversion()
  sumProgram()
  stringPractice()
  checkKeyword()
