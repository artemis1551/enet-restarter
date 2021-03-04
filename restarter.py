import subprocess
import time
from time import sleep
#(C) Artemis
#MIT License

print("ENET Restarter - Artemis#1551")
print("If you have any question, DM Me!")
filename = input("ENET Name (enet.exe)  : ")
print(f'Starting {filename} please wait...')
sleep(5)
while True:
    p = subprocess.Popen('exe '+filename, shell=True).wait()
    if p != 0:
        continue
    else:
        print(f'Theres no file named {filename}')
        break