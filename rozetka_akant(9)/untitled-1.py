from itertools import cycle
import dn_setting

'''
with open("tit.txt", "w") as file:
    for i in title:
        print(i, file=file, sep="\n")
    print("ку-ку", file=file, sep="\n")


main_keys = []
f = open('main_keys.txt')
main_keys = f.readline()

rout_keys = []
f = open('rout_keys.txt')
rout_keys = f.readlines()

iterator_rout_keys = cycle(rout_keys)
for i in range(5):
    print(f'{main_keys[:-1]}, {next(iterator_rout_keys)}')'''


for i in dn_setting.rolet:
    print(i[1], i[2], sep = '       ')