import socket
from pyfiglet import Figlet

f = Figlet(font="standard")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f.renderText("Komutan Logar"))
print(f.renderText("Port Checker / Finder"))
checkorfind = int(input("Port Checker: 1, Port Finder: 2 "))

if checkorfind == 1:
    while True:
     ip = input("What is your enemy ip? ")
     port = input("What is your enemy port? ")
     try:
        s.connect((ip, port))
        print("(YES) Port is active " + port)
     except:
        print("(NO ) Port is deactive " + port)
elif checkorfind == 2:
    while True:
        ip = input("What is your enemy ip?")
        for port in range(1, 9999 + 1):
            try:
                s.connect((ip, port))
                print("(YES) Port is active " + str(port))
                f = open("openport.txt", "x")
                f.write(port)
            except:
                print("(NO) Port is deactive " + str(port))
                


