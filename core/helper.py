#!/usr/bin/env python3

WW = '\033[1;77m'
WHITE = '\033[0m'
ENDC = '\033[0m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
GENERIC = '\033[0;33m'
CYAN = '\033[1;34m'

def info_general(string):
    print("{0}[*] {1}{2}{3}".format(CYAN,WHITE,string,ENDC))

def info_error(string):
    print("{0}[-] {1}{2}{3}".format(RED,WHITE,string,ENDC))
    
def info_warning(string):
    print("{0}[!] {1}{2}{3}".format(YELLOW,WHITE,string,ENDC))
    
def info_success(string):
    print("{0}[+] {1}{2}{3}".format(GREEN,WHITE,string,ENDC))
    
def info_question(string):
    print("{0}[?] {1}{2}{3}".format(WW,WHITE,string,ENDC))
    
def info_info(string):
    print("{0}[i] {1}{2}{3}".format(WW,WHITE,string,ENDC))
    
def info_command(string):
    print("{0}[#] {1}{2}{3}".format(WW,WHITE,string,ENDC))
