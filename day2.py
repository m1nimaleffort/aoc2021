my_file = open("directions.txt")
content = my_file.read()
content_list = content.splitlines()
my_file.close()

def position():
    depth = 0
    horizontal = 0
    a = 0
    while a < len(content_list):
        if content_list[a].split()[0] == "forward":
            horizontal = horizontal + float(content_list[a].split()[1])
        elif content_list[a].split()[0] == "up":
            depth = depth - float(content_list[a].split()[1])
        else :
            depth = depth + float(content_list[a].split()[1])
        a = a + 1

    print(horizontal)
    print(depth)
    print(horizontal * depth)

#position()

def position_aim():
    depth = 0
    horizontal = 0
    aim = 0
    a = 0
    while a < len(content_list):
        if content_list[a].split()[0] == "forward":
            horizontal = horizontal + float(content_list[a].split()[1])
            depth = depth + (aim * float(content_list[a].split()[1]))
        elif content_list[a].split()[0] == "up":
            aim = aim - float(content_list[a].split()[1])
        else :
            aim = aim + float(content_list[a].split()[1])
        a = a + 1

    print(horizontal)
    print(depth)
    print(horizontal * depth)

position_aim()
