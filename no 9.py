amount_list=int(input("Input the amount of list"))
word_list=[]
def word():
    for i in range(amount_list):
        word1=str(input("Insert a word"))
        word_list.append(word1)
        i+=1
        print(word_list)

word()
for z in word_list:
    print("Length of "+z+" "+str(len(z)))

