from time import sleep as sl
import random

i=0

math = random.randint(1, 3)

while i<=100:
    i = i + random.randint(1,20)
    print(f"Чекаем твою мать... ({str(i)}%)")
    sl(0.5)

if math == 2:
    print("Ваша мать в канаве")
elif math == 1:
    print("С вашей мамой всё в порядке, будьте спокойны!")
else:
    print('Вашу мать ебут 4 негра")

exit()
