my_file = open("input.txt")
content = my_file.read()
content_list = content.splitlines()
my_file.close()

#print(content_list)
#print(len(content_list))

def increase_counter():
    a = 1
    b = 0
    while a < len(content_list):
        if content_list[a] > content_list[a - 1]:
            b = b + 1
        a = a + 1
    print(b)
    print(a)

#increase_counter()

def triple_counter():
    a = 1
    b = 0
    while a < (len(content_list) - 2):
        if (float(content_list[a]) + float(content_list[a + 1]) + float(content_list[a + 2])) > (float(content_list[a - 1]) + float(content_list[a]) + float(content_list[a + 1])):
            b = b + 1
        a = a + 1
    print(b)

triple_counter()
