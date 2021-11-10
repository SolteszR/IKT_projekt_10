import random
import time

dobas_input = int(input('tipplej hanyast dobtam?'))

for ciklus in range(6):
        x = random.randint(1,6)
    if dobas_input == x :
        print(x, 'talált')
    else:
        


        print(x,'nem talált')
        time.sleep(0.2)