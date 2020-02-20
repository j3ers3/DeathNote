# encoding:utf-8
import os
import string
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def ran_str():
    return ''.join(random.sample(string.ascii_letters + string.digits, 4))


def say_no():
    print("[x] Your input is error! ")


def help():
    print(""" 
    Command           Description
    -------           -----------
    help              Displays the help menu.
    list              Lists modules.
    info              Displays information about one modules.
    banner            Display banner.
    version           Show the framework version.
    clear             Clear.
    back              Move back from the current context.
    exit              Exit DeathNote.
    !                 Execute Command
    q                 Exit DeathNote.
""")
