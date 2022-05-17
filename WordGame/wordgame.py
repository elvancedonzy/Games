#Importing the relevant modules
import time

print("Welcome to my the Game!!!")
name = input("What is your name: ")
age = int(input ("What is your age: "))


print("\nHello", name, "You are", age, "years old")

health = 60

if age >=18:
    print("You are old enough to play!")    
    wants_to_play = input("\nDo you want to play?(yes/no): ").lower()
    if wants_to_play == "yes":
          print("Let's play!")

          print ("You have", health, "health")

          ans = input("First choice.. Left or Right (left/right)?")
          if ans == "left":
            ans  = input("\nNice, You at the end of a road and see a river do you (jump/walk) over it: ")

            if ans == "jump":
              ans =input("\nNice, You are at a park and see a stanger do you (follow/run) him/her: ")

          
              

              if ans == "run":
                 print("\nNice..")
              elif ans =="follow":
                health -=20
                print("\nYou were kidnapped. You manage to escape but,you lost 20 health.")

              ans = input("You see someone with an ice-cream do you (steal/ask) for it: ")

              if ans == "ask":
                   print("\nNice.. ")
              elif ans == "steal":
                  health-=20
                  print("\nYou were caught and beat up. You also lost 20 health ")
 
              ans = input("\nYou get to your house do climb the (wall/stairs): ")

              if ans =="stairs":
                    print("Congats.. You win")
              elif ans =="wall":
                    health -=20
                    print("\nYou tried to climb the wall but, fell and lost 20 health ")
                    if health <=0:
                      print ("You lose")
                    else:
                      print("You win")
                  
                
                  
              else:
                print("Wrong answer")
                health -=50
                print("You lose")
                
            else:
              print("You manage to get across but lot all your health")
              health -=25  
          else:
            print ("You fell")
    else:
              print("Thanks for coming")
else:
    print ("you are not old enough to play!")

#Sleep for 10 seconds
time.sleep(10)