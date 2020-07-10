import random
import time

class Kumanda():

    def __init__(self,tv_situation = "Kapalı",tv_volume = 0,channel_list = ["BBC"],channel = "BBC"):
        self.tv_situation = tv_situation
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel
    def tv_open(self):
        if(self.tv_situation == "Open"):
            print("TV is already on...")
        else:
            print("Television turns on....")
            self.tv_situation = "Open"
    def tv_close(self):
        if(self.tv_situation == "Close"):
            print("Television turns off...")
        else:
            print("Television turns off....")
        self.tv_situation = "Close"
    def sound_settings(self):
        while True:
            response = input("Decrease the sound: '<\nIncrease sound: '>'\nExit: exit")
            if(response == "<"):
                if(self.tv_volume != 0):
                    self.tv_volume -= 1
                    print("Volume:",self.tv_volume)
            elif(response == ">"):
                if(self.tv_volume != 31):
                    self.tv_volume +=1
                    print("Volume:",self.tv_volume)
            else:
                print("Sound updated...",self.tv_volume)
                break
    def add_channel(self,channel_name):
        print("Adding channel....")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("Channel added...")
    def random_channel(self):
        random = random.randint(0,len(self.channel_list)-1)
        self.channel = self.channel_list[random]
        print("Current channel:",self.channel)
    def __len__(self):
        return len(self.channel_list)
    def __str__(self):
        return "Tv situation: {}\nTv volume: {}\nChannel list: {}\nCurrent channel: {}\n".format(self.tv_situation,self.tv_volume,self.channel_list,self.channel)
command = Command()

print("""
Television Program

1.Tv On
2.Tv Off
3.Sound Option
4.Add Channel
5.Learning the Number of Channels
6.Switch to Random Channel
7.Television Information
Press q to exit...
""")
while True:
    process = input("Choose Action:")
    if(process == "q"):
        print("The program ends..")
        break
    elif(process == "1"):
        command.tv_open()
    elif(process == "2"):
        command.tv_off()
    elif(process == "3"):
        command.sound_settings()
    elif(process == "4"):
        channel_list = input("Enter channel names separated by ',':")
        channel_list = channel_list.split(",")
        for will_be_added in channel_list:
            command.add_channel(will_be_added)
    elif(process == "5"):
        print("Number of Channels:",len(command))
    elif(process == "6"):
        kumanda.random_channel()
    elif(process == "7"):
        print(command)
    else:
        print("Invalid Transaction....")
