import time

#Create a sum count
sum=0
#Ask user for input
y=int(input())
#Creates a range between 0 and n number
for x in range (0,y+1):
#Skips number divisible by 5
  if x%5!=0:
#Skips number divisible by 7
    if x%7!=0:
#Sums up number
      sum=sum+x
#Prints out sum
print("Sum of number", sum)

#Sleep for 10 seconds
time.sleep(10)