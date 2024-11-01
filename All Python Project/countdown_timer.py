import time
def countdown_timer(seconds):
    while(seconds>0):
        minutes = seconds//60
        sec = seconds%60
        timer_formate = f"{minutes:02}:{sec:02}"
        print(timer_formate,end = "\r")
        time.sleep(1)
        seconds = seconds-1

    print("Time's up: ")

try:
    total_time=int(input("Enter time in seconds: "))
    countdown_timer(total_time)
except ValueError:
    print("Please enter valid number: ")