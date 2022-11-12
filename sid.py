import os
import aminofix
client=aminofix.Client()
e=input("EMAIL: ")
p=input("PASSWORD: ")
client.login(e,p)
os.system("clear")
print(f"{client.device_id}\n")
print(f"{client.sid}")