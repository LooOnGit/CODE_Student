dict_1 = dict()
dict_con = dict()
list = []

while True:
    UID = input("Nhập UID:")
    Filename = input("Cho xin cái tên đi: ")
    #kiểm tra ban đầu
    if len(dict_1) == 0:
        if len(dict_con) == 0:
            dict_con["UID"] = UID
            dict_con["Filename"] = Filename
        if len(list) == 0:
            list.append(dict_con)
            dict_1["Device Manager"] = list
    else:
        #kiểm tra cập nhập
        for key, value in dict_1.items():
            for i in range(0, len(value)):
                if value[i]["UID"] == UID:
                    dict_1[key][i]["Filename"] = Filename
                else:
                    dict_con["UID"] = UID
                    dict_con["Filename"] = Filename
                    dict_1[key].append(dict_con)
            print(dict_1)
                

        
    
    

    

