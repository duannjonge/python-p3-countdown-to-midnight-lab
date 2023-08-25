# your code goes here!
# function definition
# def countdown(number):
#     while number<=5 and number >=1:
#         print(f"{number} SECOND(S)!")
#         number-=1

# countdown(5)
# print("HAPPY NEW YEAR!")
import time
def countdown(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        number -= 1
        
    print("HAPPY NEW YEAR!") 


countdown(10)

def countdown_with_sleep(num):
  while num>0:
    print(f"{num} HAPPY NEW YEAR!")
    num-=1
    time.sleep(1)
  return "HAPPY NEW YEAR!"
countdown_with_sleep(5)
