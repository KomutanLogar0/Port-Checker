import socket
from pyfiglet import Figlet

f = Figlet(font="standard")
soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f.renderText("Komutan Logar"))
print(f.renderText("Pfinder"))
print("''Güneş tepeden vuruyosa gölge ayağımızın altıdır''")
checkyadafind = int(input("Port Checker: 1, Port Finder: 2 "))



if checkyadafind == 1:
    while True:
     ip = input("Düşman IP? ")
     port = input("Düşman Port? ")
     try:
        soket.connect((ip, port))
        print("(E) Port aktif " + port)
     except:
        print("(H) Port deaktif " + port)
elif checkyadafind == 2:
    while True:
        ip = input("Düşman IP?")
        for port in range(1, 9999 + 1):
            try:
                soket.connect((ip, port))
                print("(E) Port aktif " + str(port))
                f = open("openport.txt", "x")
                f.write(port)
            except:
                print("(H) Port deaktif " + str(port))
