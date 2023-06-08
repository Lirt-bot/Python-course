import random
rnumber=random.randint(1, 101)
print (rnumber)
print ("Gissa talet")
print ("Du ska gissa ett tal från 1-100, varsågod")
while (True) :
    number = int(input("skriv in ett tal:"))

    if number < 1 or number > 100 :
     print ("du måste ange ett tal som är mellan 1-100")
     print()
    else :
     if number > rnumber :
        if abs (number - rnumber) <5:
         print ("prova ett mindre tal men du är nära!")
         print()
        else:
         print ("talet är för stort prova ett mindre tal")
         print()
     elif number < rnumber :
        if abs (number - rnumber) <5:
            print("prova ett större tal men du är nära!")
            print()
        else :
            print ("taler är för litet prova ett större tal")
            print()
     elif number == rnumber :
        print ("det var rätt!")
        print()
        break








input ("enter för att avsluta")