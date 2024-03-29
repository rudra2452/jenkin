import pickle
file = open("store.txt","rb")

l=pickle.load(file)
print(l)