my_file = open("power.txt")
content = my_file.read()
content_list = content.splitlines()
my_file.close()

#print(len(content_list[0]))

def consumption():
    temp_list = []
    gamma = []
    a = 0   #list index
    b = 0   #char index
    while b < len(content_list[a]):
        while a < len(content_list):
            temp_list.append(content_list[a][b])
            a = a + 1
        if temp_list.count("1") > temp_list.count("0"):
            gamma.append("1")
        else:
            gamma.append("0")
        b = b + 1
        a = 0
        temp_list = []
    print(gamma)
    #print(temp_list.count("1"))
    #print(temp_list.count("0"))
    #print(temp_list)

#consumption()

def oxygen():
    res = content_list.copy()
    temp_list = []
    a = 0   # list index
    b = 0   # char index
    while len(res) > 1:
        while a < len(res):
            temp_list.append(res[a][b])
            a = a + 1
        a = 0
        if temp_list.count("1") >= temp_list.count("0"):
            while a < len(res):
                if res[a][b] == "0":
                    del res[a]
                else:
                    a = a + 1
        else:
            while a < len(res):
                if res[a][b] == "1":
                    del res[a]
                else:
                    a = a + 1
        a = 0
        b = b + 1
        temp_list = []
    print(res)

oxygen()

def co2():
    res = content_list.copy()
    temp_list = []
    a = 0   # list index
    b = 0   # char index
    while len(res) > 1:
        while a < len(res):
            temp_list.append(res[a][b])
            a = a + 1
        a = 0
        if temp_list.count("1") >= temp_list.count("0"):
            while a < len(res):
                if res[a][b] == "1":
                    del res[a]
                else:
                    a = a + 1
        else:
            while a < len(res):
                if res[a][b] == "0":
                    del res[a]
                else:
                    a = a + 1
        a = 0
        b = b + 1
        temp_list = []
    print(res)

co2()
