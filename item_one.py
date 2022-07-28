# DBA Pre-Employment Coding Examinations - Item Number 1
# Author: Nicole Marcial

#Initializing the elements of the array
arr = [5, 1, 4, 6, 7, 3, 5, 7, 3] 

#Loop to traverse the array and comparing its elements
for x in range (0, len(arr)):
  for y in range (x+1, len(arr)):
    if arr[x] == arr[y]:
    	print(arr[y])  
