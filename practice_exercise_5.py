list1 = [101, 105, 102, 101, 108, 105, 110]
dict = {}
for item in list1:
    if item in dict:
        dict[item] += 1
    else:
      print(item)
      dict[item] = 1
      
employees = [
  (101, "Zola", 50000),
  (102, "Carla", 65000),
  (103, "Patrick", 45000)
]

userid = int(input("Enter the employee ID: "))
for employee in employees:
  if employee[0] == userid:
    print(f"Employee Id: {employee[0]}, Employee Name: {employee[1]}, Salary: {employee[2]}")
    break
  else:
    print("Employee not found.")