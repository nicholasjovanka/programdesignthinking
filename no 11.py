sentence="the quick brown fox jumps over the lazy dog"
alphabet=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
string=sentence.replace(" ","")
newlist=[]
for i in alphabet:
    for z in string:
        if i==z:
            b="True"
            newlist.append(b)
            break
if len(newlist)>=26:
    print("Its a pangram")
else:
    print("its not a pangram")



