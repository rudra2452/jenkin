import pickle

data = {'name': 'prem', 'goal': 'to increase salary', 'city': 'New Delhi'}
with open('store.txt','wb') as file:
    pickle.dump(data,file)
          