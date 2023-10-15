def dit():
    for i in range(4):
        k = input("Enter the keys of the dictionary :")
        v = input("Enter the values of the dictionary :")
        d = {k:v for (k,v) in zip(k,v)}
        return d