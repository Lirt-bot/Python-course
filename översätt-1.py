svCmp = str.maketrans ("ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖåäÖ", 
                       "abcdefghijklmnopqrstuvwxyz{|}{|}")

def compare (s):
    return s.translate(svCmp)
personer= ["Åberg", "Öberg", "Viklund", "andersson","Andersberg", "Ärleskog","Sträng" , "Stråby","viklander"]
print (personer.sort (key=compare))