list1=[]
blank=""
def generate_n_chars():
    word=str(input("Insert a word"))
    num=int(input("Insert number"))
    for i in range(0,num):
        list1.append(word)
    print(blank.join(list1))

generate_n_chars()
