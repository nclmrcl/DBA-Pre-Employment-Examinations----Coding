# DBA Pre-Employment Coding Examinations - Item Number 3
# Author: Nicole Marcial

#Function for getting the sum
def get_sum(first_num, second_num):
  sum = first_num + second_num
  
  return sum

#Function for getting the percentage
def get_percentage(part, whole):
  percentage = "{:.2f}".format(100 * (float(part)/float(whole)))
  
  return str(percentage) + "%"

#Getting the input of the user for newly hired
counter = True;
while counter == True:
  try:
    newly_hired_male = int(input("Please enter the number of newly hired males: "))
    while counter == True:
      try:
        newly_hired_female = int(input("Please enter the number of newly hired females: "))
        while counter == True:
          try:
            permanent_pos_male = int(input("Please enter the number of permanent position males: "))
            while counter == True:
              try:
                permanent_pos_female = int(input("Please enter the number of permanent position females: "))
                while counter == True:
                  try:
                    resigned_male = int(input("Please enter the number of resigned males: "))
                    while counter == True:
                      try:
                        resigned_female = int(input("Please enter the number of resigned females: "))
                        while counter == True:
                          try:
                            counter = False
                            print("Thank you for the information! Please wait for the summary. \n")
                            print("-----------------------------------------------------------")
                            print("Here are the summary and results: \n")
                          except:
                            print(e)
                      except:
                        print("Input cannot be null and should be an integer \n")
                  except:
                    print("Input cannot be null and should be an integer \n")
              except:
                print("Input cannot be null and should be an integer \n")
          except:
            print("Input cannot be nul and should be an integer \n")
      except:
            print("Input cannot be null and should be an integer \n")
  except:
        print("Input cannot be null and should be an integer \n")

#Passing the elements to the functions and printing the results   
hired_emp = get_sum(newly_hired_male, newly_hired_female)
print("Number of newly hired employee/s:",hired_emp)
percentage = get_percentage(newly_hired_male, hired_emp)
print(str(newly_hired_male)+ " Male/s: " +percentage);
percentage = get_percentage(newly_hired_female, hired_emp)
print(str(newly_hired_female) + " Female/s: " +percentage);

permanent_emp = get_sum(permanent_pos_male, permanent_pos_female)
print("\nNumber of permanent employee/s:",permanent_emp)
percentage = get_percentage(permanent_pos_male, permanent_emp)
print(str(permanent_pos_male)+ " Male/s: " +percentage);
percentage = get_percentage(permanent_pos_female, permanent_emp)
print(str(permanent_pos_female)+ " Female/s: " +percentage);

resigned_emp = get_sum(resigned_male, resigned_female)
print("\nNumber of resigned employee/s:", resigned_emp)
percentage = get_percentage(resigned_male, resigned_emp)
print(str(resigned_male)+ " Male/s: " +percentage);
percentage = get_percentage(resigned_female, resigned_emp)
print(str(resigned_female)+ " Female/s: " +percentage);