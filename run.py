import socket, os, time
  
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer Name is:" + hostname)   
print("Your Computer IP Address is:" + IPAddr)   

time.sleep(2)

os.system("python3 eggshell.py")
