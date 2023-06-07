from random import randrange
from time import perf_counter
def urvalssorts (list):
    for j in range(1, len(list)-1):
        mintal = list[j]
        plats = j
        for i in range (j+1,len(list)):
            if list[i] < mintal:
                mintal =list [i]
                plats = i
        list [j], list[plats] = list[plats], list[j]
antal = int(input("hur många tal vill du sortera? "))
list= [randrange (1,101) for i in range(antal)]
t0=perf_counter ()
urvalssorts (list)
t1=perf_counter()
print ("att sortera {:d} heltag tog {:.3f}\ sekunder" .format (antal, t1 -t0))