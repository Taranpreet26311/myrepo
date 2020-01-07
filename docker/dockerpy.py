import os





def getports():
    container_list = input("Enter container names seperated by space: ")
    list  = container_list.split()
    print("The open port/ports are")
    count = 1
    if len(list) == 1:
        for container_name in list:
            print("Container ports are :")
            os.system("docker port "+ container_name)

    else:
        for container_name in list:
            print("Container "+ str(count) + " ports:")
            count+=1
            os.system("docker port "+ container_name)
    return "Process finished"

getports()