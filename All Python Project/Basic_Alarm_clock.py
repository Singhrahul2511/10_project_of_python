#importing time to make cpu sleep for 1 second while checking loop for alarm
import time
#taking currect_time from system to comapre the alarm time
from datetime import datetime
#defining a function to set_alarm with two arguments alarm_time and message
def set_alarm(alarm_time,message):
    #after setting alarm print the time for wating to run alarm
    print(f"Alarm set for{alarm_time} waiting..... ")
    #runing a loop to fetch curr_time and to check current_time = alarm_time
    while True:
        current_time = datetime.now().strftime("%H:%M")

        if(current_time==alarm_time):
            print(f"Alarm! {message}: ")
            #brak alfter current_time = alarm_time to decrease the over loop runnig
            break
        time.sleep(1)

alarm_time = input("Enter time to set alarm in formate of(HH:MM): ")
message = input("Enter message to be displayed after alarm off: ")
#call the function
set_alarm(alarm_time, message)

