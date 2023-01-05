#!/usr/bin/python3
import os

tools = 'nano vim git wget figlet toilet curl zip apache2 net-tools php nmap ruby libminizip1 libgtkglext1 python python3 python3-pip python3-tk python3-dev'
module = 'ansible DateTime Flask Pillow PyAutoGUI pyfiglet requests tbomb termcolor urllib3 colorama'
ngrok = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
ngrok_key = '< Auth token >'
anydesk = 'https://download.anydesk.com/linux/anydesk_6.1.1-1_amd64.deb'
visualstudio = 'https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64'

main_menu_items = [
    "[a] Update & Install tools:- This option will update the system and install a list of commonly used tools and libraries.",
    "[b] Download and Configure Ngrok:- This option will download and install Ngrok, a tool for creating secure tunnels to localhost.",
    "[c] Install Wine 7.0:- This option will install Wine 7.0, a compatibility layer that allows users to run Windows applications on Linux.",
    "[d] Install Anydesk:- This option will download and install Anydesk, a remote desktop application.",
    "[e] Install Whatsapp:- This option will install Whatsapp for Linux using the Snap package manager.",
    "[f] Install Visual Studio Code:- This option will download and install Visual Studio Code, a popular code editor.",
    "[g] Install Slack:- This option will install Slack, a communication and collaboration platform, using the Snap package manager.",
    "[h] Install Tag Sync:- This option will clone the Tag Sync repository from GitHub and install it.",
    "[i] Clean and Clear:- This option will remove any unused or broken packages and clear the system's cache.",
    "[q] Quit:- This option will exit the program.",
]

def Clean():
    os.system('sudo apt -y autoremove')
    os.system('sudo apt -y autoclean')

def Update():
    os.system('sudo apt -y update')
    os.system('sudo apt -y install '+tools)
    os.system('sudo apt -y --fix-broken install')
    os.system('sudo gem install lolcat')
    os.system('pip install '+module)

def Ngrok():
    os.system('wget '+ngrok)
    os.system('unzip ngrok-stable-linux-amd64.zip')
    os.system('rm -fr ngrok-stable-linux-amd64.zip')
    os.system('sudo mv ngrok /usr/bin/')
    os.system('ngrok '+ngrok_key)
    os.system('sudo ngrok '+ngrok_key)

def Wine():
    os.system('sudo dpkg --add-architecture i386')
    os.system('wget -qO - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -')
    os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'")
    os.system('sudo apt -y update')
    os.system('sudo apt install --install-recommends winehq-stable')
    os.system('wine --version')

def Anydesk():
    os.system('wget '+anydesk)
    os.system('sudo dpkg -i *.deb')
    os.system('sudo rm -frv *.deb')

def Whatsapp():
    os.system('sudo apt -y install snapd')
    os.system('sudo snap install whatsapp-for-linux')

def VisualStudio():
    os.system('wget '+visualstudio)
    os.system('sudo dpkg -i *.deb')
    os.system('sudo rm -frv *.deb')

def Slack():
    os.system('sudo apt -y install snapd')
    os.system('sudo snap install slack')

def Tag_Sync():
    os.system('git clone https://github.com/AdeshSingh7/tag-sync.git')
