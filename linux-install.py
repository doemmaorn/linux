from sys import *
from time import sleep
from os import system
gray="\033[1;30m"
white="\033[1;37m"
yellow="\033[1;33m"
Blue="\033[1;34m"
blue="\033[1;34m"
red="\033[1;31m"
green="\033[1;32m"
cyan="\033[1;36m"
system('clear')
def jalan(x):
    for i in x+"\n":
        stdout.write(i)
        stdout.flush()
        sleep(0.04)
logo=f"""
{yellow}==========================================================================
{yellow}[{white} .o88b.  .d88b.  d8888b. d88888b{gray} d8888b. db       .d8b.   .o88b. db   dD{yellow}]
{yellow}[{white}d8P  Y8 .8P  Y8. 88  `8D 88'     {gray}88  `8D 88      d8' `8b d8P  Y8 88 ,8P'{yellow}]
{yellow}[{white}8P      88    88 88   88 88ooooo {gray}88oooY' 88      88ooo88 8P      88,8P  {yellow}]
{yellow}[{white}8b      88    88 88   88 88~~~~~ {gray}88~~~b. 88      88~~~88 8b      88`8b  {yellow}]
{yellow}[{white}Y8b  d8 `8b  d8' 88  .8D 88.     {gray}88   8D 88booo. 88   88 Y8b  d8 88 `88.{yellow}]
{yellow}[{white} `Y88P'  `Y88P'  Y8888D' Y88888P {gray}Y8888P' Y88888P YP   YP  `Y88P' YP   YD{yellow}]
{yellow}==========================================================================
"""
con1=f"""
                                          
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█{white}[{red}*{white}]{red}Github:{red}https://github.com/doemmaorn \033[33m█
█{white}[{green}*{white}]{yellow}Whatsapp:{green}+212 762294391{blue}
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""
con=f"""
                                          
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█{white}[{green}*{white}]{Blue}Github:{red}https://github.com/bash-sh900 \033[33m█
█{white}[{green}*{white}]{Blue}Whatsapp:{red}+212 642663312{yellow}
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""

jalan(logo)
jalan(con1)
jalan(con)
import os
print("01--------------------------Kali ")
print("02--------------------------Ubuntu")
print("03--------------------------Alpine")
print("04--------------------------Manjaro")
print("05--------------------------Fedora")
print("06--------------------------Debian")
print("07--------------------------Arch")
print("08--------------MY ACCOUNT FACEBOOK :")
print("09--------------WE GROUP WHATSAPP :")
loop=input("       Chopse options :")

if loop=="1":
    system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh | bash .")
if loop=="2":
    system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20.sh | bash")
if loop=="3":
    system("pkg update -y && pkg install curl proot tar -y && curlhttps://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh | bash")
if loop=="4":
    system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro.sh | bash")
if loop=="5":
    system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh | bash")
if loop=="6":
    system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh | bash")
if loop=="7":
    system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh | bash")
if loop=="8":
    system("xdg-open https://www.facebook.com/profile.php?id=100056034938684")
if loop=="9":
        system("xdg-open https://chat.whatsapp.com/GSxgjtoyTAhKvpwLgeLvK6")