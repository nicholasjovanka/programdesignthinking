finalword=""
word=str(input("Insert a word"))
vowel=["a","i","u","e","o"]
consonant=["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

def consocheck(x):
    for b in consonant:
        if x==b:
            return True
        break
    else:
        return False
def vowelcheck(x):
    for d in vowel:
        if x==d:
            return True
        break
    else:
        return False


if word[len(word)-2:len(word)+1]=="ie":
    word=word[:-2]
    finalword=word+"y"+"ing"
elif word[-1]=="e":
    word=word[:-1]
    finalword=word+"ing"
elif consocheck(word[-1])==True and vowelcheck(word[-2])==True and consocheck(word[-3])==True:
    finalword=word+word[-1]+"ing"
else:
    finalword=word+"ing"

print(finalword)








