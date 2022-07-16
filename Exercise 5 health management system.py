print("Welcome to Health Management system .!!(Swaasth prabandh pranali me apka swagat hai)")
client_list={1:"Rohan",2:"Harry",3:"Hammad"}
log_list={1:"Food",2:"Exercise"}
def getTime():
    import datetime
    return datetime.datetime.now()
def setData():
    print("Enter the client number for which you want to log the information:\n"
          "1 for Rohan,\n"
          "2 for Harry,\n"
          "3 for Hammad:")
    client_choice=int(input())
    print("What information do you want to log for",client_list[client_choice],":")
    print("Enetr 1 for food or 2 for exercise:")
    info_choice=int(input())
    if(info_choice==1):
        f=open(client_list[client_choice]+"_Food.txt","w")
        print("Please enter the information about",log_list[info_choice],":")
    elif info_choice==2:
        f = open(client_list[client_choice] + "_Exercise.txt", "w")
        print("Please enter the information about", log_list[info_choice], ":")
    infor="["+getTime().strftime("(%H:%M:%S.%f)")+"]"+input()
    f.write(infor)
    print("Information has been logged successfully.!!\n")
    f.close()
def getData():
    print("Enter the client number for which you want to check the information:\n"
              "1 for Rohan,\n"
              "2 for Harry,\n"
              "3 for Hammad:")
    client_choice=int(input())
    print("What information do you want to check for",client_list[client_choice],":")
    print("Enetr 1 for food or 2 for exercise:")
    info_choice=int(input())
    try:
        if(info_choice==1):
            f=open(client_list[client_choice]+"_Food.txt","r")
            print(f.read(),"\n")
            print("Information has been fetched successfully.!!\n")
            f.close()
        elif info_choice==2:
            f = open(client_list[client_choice] + "_Exercise.txt", "r")
            print(f.read(),"\n")
            print("Information has been fetched successfully.!!\n")
            f.close()
    except:
        print("No information available.!!")
while(True):
    print("Please let us know what do you wish to do. Please press \n"
          "1. For logging the information.\n"
          "2. For checking the information.\n"
          "3. For Exit.")
    action_needed=int(input())
    if(action_needed==1):
        setData()
    elif(action_needed==2):
        getData()
    elif action_needed==3:
        print("See you sooooooon.!!!!")
        exit()
    else:
        print("Wrong input. Please try again")