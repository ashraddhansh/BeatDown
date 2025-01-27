import time
import os
import sys
import subprocess
from pyfiglet import Figlet
f = Figlet(font='larry3d')

def countdown_timer(inputMinute, inputSecond):
    totalTime = inputMinute*60+inputSecond

    mpv_process = subprocess.Popen(['mpv', '--no-video', '--no-terminal', 'https://www.youtube.com/watch?v=LY_rMXXuJp8'])


    for i in range(totalTime, -1 ,-1):
        os.system("clear")
        realMinute = i//60
        realSeconds = i%60

        time_str = f"{realMinute:02}:{realSeconds:02}"
        print(f.renderText(time_str))
        time.sleep(1)
    mpv_process.terminate()


if __name__== "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <minutes> <seconds>")
        sys.exit(1)

    try:
        minutes = int(sys.argv[1])
        seconds = int(sys.argv[2])
        countdown_timer(minutes, seconds)

    except ValueError:
        print("Please provide valid integers for both inputs!")



# Set the countdown duration in seconds





# first i need to ask for the time for timer.
# then convert that into minutes and seconds.
# then start the countdown in minutes and seconds.
