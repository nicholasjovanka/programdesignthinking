import os
def number1():
    print(os.getcwd())
    filename=str(input("Insert the file  name"))
    filename.lower()
    file=open(filename)
    data=file.read()
    filterlist=data.split()
    newlist=[]
    for i in filterlist:
        if filterlist.count(i)==1:
            newlist.append(i)
    print(newlist)

def number2():
    filename=str(input("Insert the file name"))
    firstfile=open(filename)
    newdata=firstfile.readlines()
    newlist=[]
    z=0
    for i in newdata:
        secondfile=open("filenamecopy.txt","w")
        newlist.append(str(newdata.index(i))+" "+i.strip("\n"))
        secondfile.write(newlist[z])
        z+=1
        secondfile=open("filenamecopy.txt","r")
        print(secondfile.read())

def number3():
    filename=str(input("Insert the file name"))
    firstfile=open(filename)
    newdata=firstfile.read()
    filterlist=newdata.split()
    alphalength=0
    for i in filterlist:
        alphalength=alphalength+len(i)
    print(alphalength/len(filterlist))

def number4():
    prefixes=["Mr.","Mrs.","Dr.","Jr."]
    anotation=["i.e."]
    word=""
    filename=str(input("insert the file name "))
    file=open(filename)
    file=file.read()
    newlist=file.split()
    for i in newlist:
        temp=i+" "
        if any(i in c for c in prefixes):
            pass
        elif i.endswith(","):
            temp=temp.replace(" ","")
        elif any(i in b for b in anotation):
            pass
        elif i.endswith("!"):
            temp=temp+"\n"
        elif i.endswith("?"):
            temp=temp+"\n"
        elif i.endswith("."):
            temp=temp+"\n"
        word=word+temp
    print(word)

input1=str(input("Which number do you want to view 1/2/3/4"))
if input1=="1":
    number1()
elif input1=="2":
    number2()
elif input1=="3":
    number3()
elif input1=="4":
    number4()





