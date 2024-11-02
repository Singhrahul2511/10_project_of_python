#import time here to make a sleep of 1 sec
import time
#define a function and pass only one parameter as seconds
def countdown_timer(seconds):
    #create a loop while seconds becomes 0
    while(seconds>0):
        #minutes will count after seconds divided by 60 .not count remainder
        minutes = seconds//60
        #count remainder by sec%60 
        sec = seconds%60
        #fix timer formate up to 2 places
        timer_formate = f"{minutes:02}:{sec:02}"
        #print countdown at the same next line
        print(timer_formate,end = "\r")
        #make a sleep of 1sec
        time.sleep(1)
        #gradually reduce by 1-1 seconds
        seconds = seconds-1
#print time up while(seconds==0)
    print("Time's up: ")

try:
    total_time=int(input("Enter time in seconds: "))
    countdown_timer(total_time)
except ValueError:
    print("Please enter valid number: ")