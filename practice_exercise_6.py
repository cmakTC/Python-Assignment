def checkEvenOdd():
  num = int(input("Enter a number: "))
  if num % 2 == 0:
    print(f"{num} is even.")
  else:
    print(f"{num} is odd.")

def countVowels():
  string = input("Enter a string: ").lower()
  vowels = "aeiou"
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  print(f"The number of vowels in the string is: {count}")
  
def checkPrime():
  num = int(input("Enter a number: "))
  if num < 2:
    print(f"{num} is not prime.")
    return
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      print(f"{num} is not prime.")
      return
    print(f"{num} is prime.")
    
def avgMarks():
  marks = input("Enter marks separated by spaces: ").split()
  marks = [float(mark) for mark in marks]
  average = sum(marks) / len(marks)
  print(f"The average of the marks is: {average}")
  
  def main():
    checkEvenOdd()
    countVowels()
    checkPrime()
    avgMarks()