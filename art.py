import time
import os
from art import text2art

def countdownTimer(seconds):
    for i in range(seconds, -1, -1):
        os.system("clear")
        ascii_art = text2art(str(i))
        print(ascii_art)
        time.sleep(1)

countdownTimer(10)

# first i need to take input from the user.
# then convert the time into minutes and seconds.
