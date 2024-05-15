import random
import sqlite3
boh = 0
pis = 0
money = 0
hp = 0
dmg = 0
point = 0
strong = 0
armor = 0
magic = 0
xpned = 0
xpneed = 0
conn = sqlite3.connect('save.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS SAVE(SBK INT,
boh INT,
pis INT,
money INT,
hp INT,
dmg INT,
point INT,
strong INT,
armor INT,
magic INT,
xpned INT,
xpneed INT)''')
def menu():
    print('1)start \n 2)help \n 3)exit \n 4)save \n 5)load \n 6)IDEAS HERE! \n 7)Items \n 8)Shop')
    starthelp = input()
    return starthelp
# def start():
    
def shop(money, boh, pis):
    print('                /\     /\ \n               0000000000\n               0 0      0 0\n               0     3    0\n       _________0000000000__________\n     __00000000000000000000000000000__\n     000000000000000000000000000000000   =================================\n     00          888888888          00   I     Welcome to my shop!       I\n     00        8888888888888        00   I   There you can buy items,    I \n     00        8880 _ _ 0888 000000 00   I  You can use them in battle!  I\n     00   0      60 0 0 09      0 0 00   ================================= \n     00  000      0  -  0       000 00\n     00  000       00000          0 00   1)Bo o waer (50 money) (You have ',boh,' of it)\n     00  000        000           0 00 \n     0000---000000000000000000000---00   2)P I S T O L (100 money)(You have ',pis,' of it)\n     00000000  W e l c o m e  00000000   \n     00000000       T o       00000000   =======================================\n     00000000  J o h n y \' s  00000000   I PISTOL IN DA SHOP BAAAAAAAAAAAABIES I        \n     00000000     S H O P     00000000   =======================================\n     000000000000000000000000000000000   E to exit\n     \n       I can see your money it\'s ',money,'\n       go defeat enemies to get money!\n       i will be looking!')
shop(money, boh, pis)
def help():
    print('press numbers to attack,use items,heal or use super attacks! various monsters will be encountered on your way so be prepared and use those numbers! echo fight various bosses to get xp and items to progress through victory and eat the holy poop!')
# def save()
# while starthelp != 1:
#     starthelp = menu()
#     if starthelp == 1:
#         start()
