from telethon.sync import TelegramClient
from telethon import utils
import csv
from csv import reader
import configparser






done = False
with open('phone.csv', 'r') as f:
    str_list = [row[0] for row in csv.reader(f)]

    
    po = 0
    for pphone in str_list:
        
        
        phone = utils.parse_phone(pphone)
        po += 1
        
        
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}",2982636,'02f00ae88d292c81d64958454941c636')
        client.start(phone)
        

        client.disconnect()
        print()
    done = True

input("Done!" if done else "Error!")
