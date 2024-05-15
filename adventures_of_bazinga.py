import random
import sqlite3
conn = sqlite3.connect('save.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS SAVE(SBK INT,
boh INT,
pis INT,
money INT,
HP INT,
dmg INT,
point INT,
strong INT,
armor INT,
magic INT,
xpned INT,
xpneed INT)''')
def menu():
    print('1)start \n 2)help \n 3)exit \n 4)save \n 5)load \n 6)IDEAS HERE! \n 7)Items \n 8)Shop')
def help():
    print('press numbers to attack,use items,heal or use super attacks! various monsters will be encountered on your way so be prepared and use those numbers! echo fight various bosses to get xp and items to progress through victory and eat the holy poop!')
# def save()
endisnow = 0
# while endisnow != 1:
#     menu()