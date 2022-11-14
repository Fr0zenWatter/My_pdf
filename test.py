from os import system

od_arr = ["git add .",'git commit -m "None"',"git push"]

for od in od_arr:
    system(od)