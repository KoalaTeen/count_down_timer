import time
import easygui
import os


def clear_console():
    os.system('cls')
def countdown(days, hours, minutes, seconds):
    starttime = time.time()
    while True:
        clear_console()
        print(" D  ", "H  ", "M  ","S\n",days,':', hours,':', minutes,':', seconds)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))
        seconds = seconds - 1
        if seconds == 0:
            if minutes == 0:
                print("D", "\tH", "\tM", "\tS\n", days, ':', hours, ':', minutes, ':', seconds, '\r')
                easygui.msgbox("The countdown is over!", title="Attention!")
                break
            else:
               seconds = seconds + 59
               minutes = minutes - 1
        if minutes == 0:
            if hours > 0:
                minutes = minutes + 59
                hours = hours - 1
            else:
                minutes = 0
        if hours == 0:
            if days > 0:
                hours = hours + 23
                days = days - 1
            else:
                hours = 0