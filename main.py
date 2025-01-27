import time
import os
from pyfiglet import Figlet
f = Figlet(font='larry3d')

def countdown_timer(seconds):
    for i in range(seconds, -1, -1):
        os.system("clear")  # Clear the terminal (use 'cls' on Windows)
        #ascii_art = pyfiglet.figlet_format(str(i))
        print(f.renderText(str(i)))
        #print(ascii_art)
        time.sleep(1)

# Set the countdown duration in seconds
countdown_timer(10)
