# encoding: utf-8
import os

global purple, purple2, cyan, darkcyan, blue, green, yellow, red, bold, end

def set_color():
    global purple, purple2, cyan, darkcyan, blue, green, yellow, red, bold, end

    if os.name == "nt":
        try:
            import win_unicode_console, colorama
            win_unicode_console.enable()
            colorama.init()
        except Execption as e:
            print("[x] Please pip install win_unicode_console colorama")
            exit(1)

    purple   = '\033[95m'
    purple2  = '\033[92m'
    cyan     = '\033[96m'
    darkcyan = '\033[36m'
    blue     = '\033[94m'
    green    = '\033[32m'
    yellow   = '\033[93m'
    red      = '\033[31m'
    bold     = '\033[1m'
    end      = '\033[0m'

set_color()


def good(text):
    print(cyan + "[+] " + end + blue + text  + end )

def p_dec(text):
    print("\nDescription:" + blue + text + end )

def p_pay(text):
    print('Payload:\n' + blue + text + '\n' + end )

def p_modules(text):
    text2 = text.replace('[', red+'['+end).replace(']', red+']'+end)
    print(text2 + '\n')

def p_line(text):
    return purple2 + '[' + red + text + purple2 + ']'

def error(text):
    print(red + "[x] " + end + blue + text + end )


def bye():
    print(green + 'Bye   : )' + end )
    exit(0)
