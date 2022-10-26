import socket
from pyfiglet import Figlet

f = Figlet(font="slant")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f.renderText("Komutan Logar"))
print(f.renderText("Port Checker / Finder"))
checkorfind = int(input("Port Checker: 1, Port Finder: 2 "))


if checkorfind == 1:
    while True:
     ip = input("Düşman IP'yi giriniz.")
     port = input("Düşman Port'u giriniz.")
     try:
        s.connect((ip, port))
        print("(E) Port aktif " + port)
     except:
        print("(H) Port deaktif " + port)
elif checkorfind == 2:
    while True:
        ip = input("Düşman IP'yi giriniz.")
        for port in range(1, 9999 + 1):
            try:
                s.connect((ip, port))
                print("(Y) Port aktif" + str(port))
                f = open("openport.txt", "x")
                f.write(port)
            except:
                print("(H) Port deaktif " + str(port))
                


