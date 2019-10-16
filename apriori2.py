# Apriori

# Importing the libraries
import numpy as np
import pandas as pd
import pickle

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)


sets=[]
for i in range(len(results)):
    sets.append(results[i][0])
    
    
items_com=[list(x) for x in sets] 


# for _ in items_com:
#     print(_)
################## to write in the file .....................................
# with open('listitem2.dat','wb') as fp:
#     pickle.dump(items_com,fp)


# l3=[]
# for _ in items_com:
#     l3.append(_[0])

# st2 = set()
# for _ in l3:
#     st2.add(_)
# print("*"*55)
# print(len(st2))




