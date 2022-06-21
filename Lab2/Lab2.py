from math import pi

def problem1():
  radius = int(input("What is the radius? "))
  # Area = pi * r ^2
  area = pi * radius**2
  # Circumference = 2 * pi * r
  circumference = 2 * pi * radius

  print(f"Area: {area}\nCircumference: {circumference}")
  
def problem2():
  # Method 1
  first_name = input("What is your first name ")
  last_name = input("What is your last name? ")
  name = input("What is your full name ")

  # Method 2
  space_index = name.find(" ")
  first = name[:space_index]
  last = name[space_index + 1:]
  
  print(last_name, first_name)
  print(last_name + ' ' + first_name)
  print(last, first)

def problem3():

  n = int(input("Give a random integer "))
  print(n + n*n + n*n*n)

def problem4():
  number = int(input("Give a random integer"))
  if number % 2 == 0:
    print("Even")
  else:
    print("Odd")


def problem5():

  x = int(input("X Value: "))
  y = int(input("Y Value: "))

  print((x + y) * (x+y)**2 + 2 * x)

def problem6():
  
  miles = int(input("How many miles did you run? "))

  kilometers = miles * 1.60934

  print(f"You ran {kilometers} kilometers today!")

def problem7():

  date = input("What is today's date? MM/DD/YYYY ")
  time = input("What is the current time? HH:MM (am/pm) ")

  month = date[:2]
  # year = date[8:10]
  year = date[-2:]

  am_pm = time[-2:]
  hour = int(time[:2])
  minute = time[3:5]

  if am_pm == "pm":
    hour += 12
    # hour = hour + 12
    # hour += 12
    # hour = 3 + 12
  print(f"Hey, Soldier,\n The time is {hour}:{minute} and today\'s date is {month}/{year}!")


def problem8():

  sentence = input("Give me a sentence: ")
  upper_setnence = sentence.upper()
  
  new_sentence = upper_setnence.replace('A','8')
  output = new_sentence.replace('E', '3')

  print(output)
  # print(month)
  # print(year)
  # print(am_pm)
  # print(hour)
  # print(minute)
  # print(date)
  # print(time)
  
def main():
  # problem1()
  # problem2()
  # problem3()
  # problem4()
  # problem5()
  # problem6() 
  # problem7()
  problem8()


if __name__ == "__main__":
  main()
