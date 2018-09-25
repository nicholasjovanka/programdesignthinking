def largest():
    ind=[]
    while (len(ind)) < 3:
        num=int(input("Insert a number"))
        ind.append(num)
        print(ind)
        list.sort(ind)

    return print("The largest number is"+" "+ str(ind[-1]))





largest()
