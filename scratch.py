import random
def bubblesort(list1):
    listlenght=len(list1)-1
    i=0
    while i+1<2 :
        for b in range(listlenght):
            if list1[b]>list1[b+1]:
                temp=list1[b]
                list1[b]=list1[b+1]
                list1[b+1]=temp
                print(list1)



userinput=str(input("Do you want the number to be inputted manually or a randomized range of numbers ?(M/R)"))
if userinput.lower()=="m":
    blist=[]
    lenght=int(input("Insert the amount of numbers you want to insert"))
    for z in range(0,lenght):
        num=int(input("Insert a number"))
        blist.append(num)
    bubblesort(blist)
elif userinput.lower()=="r":
    input1=int(input("Insert the minimum range of the number"))
    input2=int(input("Insert the maximum range of the number"))
    list1=[]
    for i in range(input1,input2+1):
        list1.append(i)
    random.shuffle(list1)
    print("The randomized number is"+str(list1))
    bubblesort(list1)



