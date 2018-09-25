amount_list=int(input("Input the amount of list"))
word_list=[]
def word():
    for i in range(amount_list):
        word1=str(input("Insert a word"))
        word_list.append(word1)
        i+=1
        print(word_list)

newlist=[]
word()
for z in word_list:
    newlist.append(len(z))
print(newlist)
newlist.sort()
print("The longest number is"+str(newlist[-1]))
