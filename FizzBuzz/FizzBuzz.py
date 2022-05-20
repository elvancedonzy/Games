import time
test = 0
for number in range(1,101):
  test+=number
  
  if number%3==0 and number%5==0:
   print("FizzBuzz")
  elif number%3==0:
   print("Fizz")
  elif number%5==0:
   print("Buzz")
  else:
   print(number)

# Sleep for 10 seconds
time.sleep(10)