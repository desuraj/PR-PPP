# Apriori

# Importing the libraries
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []

for i in range(0, len(dataset)):
    transactions.append([str(dataset.values[i,j]) for j in range(0, dataset.shape[1])])
#print(transactions[1])

############################################## removing pf null
# =============================================================================
trans=[]   
for _ in transactions:
    temp =[] 
    for x in _ :
        if x == 'nan':
            pass
        else:
            temp.append(x)
    trans.append(temp)
# =============================================================================
    
#############################################################################


# Training Apriori on the dataset
from apyori import apriori
rules = apriori(trans, min_support = 0.003, min_confidence = 0.02, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)
# =============================================================================
# 
# =============================================================================
#print(results[0][0])
#print(results[1])

# =============================================================================
# total items in store
# =============================================================================
total_item=[]
for _ in transactions:
    for i in _:
        if i not in total_item:
            total_item.append(i)
            
total_count_of_item = len(total_item)

# =============================================================================
# list of item combination
# =============================================================================

##### plz check
# =============================================================================
sets=[]
for i in range(len(results)):
    sets.append(results[i][0])
    


items_com=[list(x) for x in sets]
# #print(items_com)
# l1 = []
# for _ in items_com:
#     l1.append(_[0])
# 
# l1_set =set ()
# for _ in l1:
#     l1_set.add(_)
# 
# print(l1_set)
# print("*"*55)
# print(len(l1_set))
# =============================================================================

#print(len(results))
# =============================================================================
# predict item
# =============================================================================
def f1(p_name):
    #s=input('Enter item you wan to buy: ')
    s = p_name
    st =set()
    print("You can also Buy the following items......!!!\n")
    for _ in items_com:
        #print(_[0])
        if s in _[0]:
            for x in _[1:]:
                x = x.upper()
                st.add(x)
    print (list(st))
    print('\nThank you for visiting.....!!!')
    return (list(st))






















        