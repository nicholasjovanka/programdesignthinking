amount_list=int(input("Input the amount of list"))
num_list=[]
def num():
    for i in range(amount_list):
        word1=int(input("Insert a number"))
        num_list.append(word1)
        i+=1
        print(num_list)

num()
for z in num_list:
    print("*"*z)
