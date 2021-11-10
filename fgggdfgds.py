import random
import time
import os

def clear ():
    os.system('CLS')


C = int(input("hányszor pörögjön a kocka?"))

for ism in range (C):
    X = random.randint(1,6)
    print(X)
    time.sleep(1)
    clear()



print(r"""

       .-------.
      /   o   /|
     /_______/o|
     | o     | |
     |   o   |o/
     |     o |/
     '-------'
""")