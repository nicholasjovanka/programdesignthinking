def overlapping():
    a=["q","e","a","b","d"]
    b=["a","b","c","d"]
    for i in a:
        for j in b:
            if i==j:
                return True
    else:
        return False

print(overlapping())


