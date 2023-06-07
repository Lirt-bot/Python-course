from random import randrange
list = [randrange(1,101) for i in range (20)]
print (list)
mintal=list[0]
plats= 0
for i in range(1, len(list)):
    if list [i] < mintal :
        mintal = list[i]
        plats = i
print ("minsta tal = {} på plats{}" .format (mintal, plats))
list[0], list [plats] = list [plats], list [0]
print ("sedan vi bytt plats på första och minsta :") 
print (list)
for j in range(1, len(list)-1):
        mintal = list[j]
        plats = j
        for i in range (j+1,len(list)):
            if list[i] < mintal:
                mintal =list [i]
                plats = i
        list [j], list[plats] = list[plats], list[j]
        print("sorterad lista")
        print (list)
