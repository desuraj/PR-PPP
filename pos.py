import pickle

def f3(p_name1):
    ################### display items of list1
    list_items_1 = []
    with open('listitem.dat','rb') as fpr:
        list_items_1.append(pickle.load(fpr))

    # for _ in list_items_1[0]:
    #     print(_)

    l_1=[]
    for _ in list_items_1[0]:
        l_1.append(_[0])

    st_1 = set()
    for _ in l_1:
        st_1.add(_)
    # print("*"*55)
    # print(len(st_1))
    ############ display itemlist 2
    list_items_2 = []
    with open('listitem2.dat','rb') as fpr:
        list_items_2.append(pickle.load(fpr))

    # for _ in list_items_2[0]:
    #     print(_)

    l_2=[]
    for _ in list_items_2[0]:
        l_2.append(_[0])

    st_2 = set()
    for _ in l_2:
        st_2.add(_)
    # print("*"*55)
    # print(len(st_2))

    total_items=set()
    for _ in st_1:
        total_items.add(_)
        
    for _ in st_2:
        total_items.add(_)
        
    total_items_list=[]
    for _ in total_items:
        total_items_list.append(_)
        
    # print(len(total_items))


        #s=input('Enter item you wan to buy: ')
    s = p_name1
    st_1 =set()
    st_2 =set()
    flag = 0
    l1=[]
    l2=[]
    for _ in list_items_1[0]:
        if s in _[0]:
            flag = 1
            for x in _[1:]:
                if x == 'nan':
                    pass
                else:
                    x = x.upper()
                    l1.append(x)
    # print(flag)
    if flag == 0 :
        for _ in list_items_2[0]:
            if s in _[0]:
                for x in _[1:]:
                    if x == 'nan':
                        pass
                    else:
                        x = x.upper()
                        l2.append(x)
        # return (list(st_2))
    rl1=[]
    for _ in l1:
        if _ in rl1:
            pass
        else:
            rl1.append(_)

    rl2=[]
    for _ in l2:
        if _ in rl2:
            pass
        else:
            rl2.append(_)

    if flag == 1:
        return (rl1[:5])
    elif flag ==0:
        return (rl2[:5])
    