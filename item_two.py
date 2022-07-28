# DBA Pre-Employment Coding Examinations - Item Number 2
# Author: Nicole Marcial

#Getting the input of the user
while True:
  try:
      num = int(input("Please enter the number of elements you want to print: "))
      break;
  except:
    print("Input cannot be null and should be an integer \n")

#Loop to print the elements
for x in range(num):
  for y in range(x+1):
    print((x+1), end=' ')
  print()
