import pickle

def f2(p_name):
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
    s = p_name
    st_1 =set()
    st_2 =set()
    flag = 0
    for _ in list_items_1[0]:
        if s in _[0]:
            flag = 1
            for x in _[1:]:
                x = x.upper()
                st_1.add(x)
            break
    #print(list(st))
    #print(flag)
    # return (list(st_1))
    if flag == 0 :
        for _ in list_items_2[0]:
            if s in _[0]:
                for x in _[1:]:
                    x = x.upper()
                    st_2.add(x)
                break
        # return (list(st_2))
    if flag == 1:
        return (list(st_1))
    elif flag ==0:
        return (list(st_2))
    