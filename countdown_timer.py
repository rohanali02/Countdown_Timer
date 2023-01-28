import time
import msvcrt
from pygame import mixer
from os import environ
from playsound import playsound

aborted = False
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

def countdown_t_seconds(t):
    print('\nPress Esc to Exit')
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            aborted = True
            print("\n\nYou pressed Esc, so exiting... ")
            exit()
            break
            

    while True:
        mixer.init()
        mixer.music.load('D:/Rohan SMM/Python/alarm.wav')
        mixer.music.play()
        print('\nTime is up!')
        print("Do you want to stop the alarm?")
        print("1. Yes")
        print("2. No")
        choice=int(input("Enter your choice: "))
        if choice==1:
            break
        elif choice==2:
            pass
        else:
            print("Invalid Choice")

def countdown_t_minutes(t):
    print('\nPress Esc to Exit')
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            aborted = True
            print("\nYou pressed Esc, so exiting... ")
            break
        
        
    
    while True:
        mixer.init()
        mixer.music.load('D:/Rohan SMM/Python/alarm.wav')
        mixer.music.play()
        print('Time is up!')
        print("Alarm is ringing")
        print("Do you want to stop the alarm?")
        print("1. Yes")
        print("2. No")
        choice=int(input("Enter your choice: "))
        if choice==1:
            break
        elif choice==2:
            pass
        else:
            print("Invalid Choice")

print("\t\n\n **** Welcome to Countdown ****")

print("\nDo you wanna Enter time in Minutes or Seconds")
print("1. Minutes")
print("2. Seconds")
choice=int(input("\nEnter your choice: "))
if choice==1:
    t= int(input('\nEnter time in minutes: '))
    t=60*t
    countdown_t_seconds(t)
    


elif choice==2:
    t= int(input('\nEnter time in seconds: '))

    countdown_t_seconds(t)
       
else:
    print("Invalid Choice")

