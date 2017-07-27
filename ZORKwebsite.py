print "WELCOME TO ZORK 2017"
money = 0
inv = []
import random
name = raw_input("What is your name?")
choiceList1 = []
end = False
choiceTree = []
visited = False
# OBJECTS
vod = True
cloth = True
news = random.randint(0, 1)
while end == False:
    state = False
    while state == False :
            choice = raw_input("Ok, " + name + ", do you prefer the city or the country?")
            if choice == "inv" or choice == "inventory" :
                print inv
                choice = raw_input("")
            if "city" in choice :
                area = "alley"
                money = 5
                inv = [str("$" + str(money)), "paperclip"]
                print "You wake up in a dark alleyway. There are police sirens in the distance and a shiny object on the ground in a pile of rubbish."
                while area == "alley":
                    if "inv" in choice or "inventory" in choice or "stuff" in choice:
                        print "Inventory = |" + str(inv) + "|"
                    choice = raw_input("")
                    if "object" in choice and vod == True:
                        area = "object"
                        vod = False
                        choice = raw_input("You pick up the object. It is a large glass bottle with some clear liquid towards the bottom.")
                        inv.append("drink")
                        print "Inventory = |" + str(inv) + "|"
                        area = "alley"
                    if "drink" in choice and "drink" in inv :
                        choice = raw_input("You drink the clear liquid. It has a harsh taste that burns your throat.")
                    elif "rubbish" in choice :
                        area = "rubbish"
                        while area == "rubbish":
                            choice = raw_input("Your look through the rubbish. There are scraps of cloth and crumpled up newspapers.")
                            if "inv" in choice or "inventory" in choice or "stuff" in choice:
                                print "Inventory = |" + str(inv) + "|"
                            elif "back" in choice or "alley" in choice or "go back" in choice or "go back to alley" in choice :
                                area = "alley"
                            elif "cloth" in choice and cloth == True :
                                cloth = False
                                choice = raw_input("You pick up the cloth and put it in your pocket. It might come in handy later.")
                                inv.append("cloth")
                            elif "newspaper" in choice or "newspapers" in choice and news == 1:
                                news = 3
                                choice = raw_input("You pick up the newspaper.")
                                inv.append ("newspaper")
                            elif "newspaper" in choice or "newspapers" in choice and news == 0:
                                "The newspapers appears too soaked and soggy to be of any use."
                            elif "newspaper" in inv and "read" in choice and "newspaper" in choice:
                                raw_input("The New York Times, Year 2041.")
                            elif area == "rubbish" and cloth == False and news == True :
                                raw_input("There's a few crumpled up newspapers that look slightly usable.")
                            elif area == "rubbish" and cloth == True and news == False :
                                raw_input("There's some cloth that still looks usable amongst the trash.")
                            elif area == "rubbish" and cloth == False and news == False :
                                raw_input("It's just a pile of trash.")
                            else:
                                choice = raw_input("I don't understand what you mean")
            else:
                time = 360
                while time>0 :
                    while state == False :
                        if "watch" in choice and "watch" in inv:
                            print 1600 - time
                        if "country" in choice:
                            area = "start"
                            streamQuick = False
                            while area == "start" and streamQuick == False:
                                area = "start"
                                inv = ["rag", "knife",]
                                choice = raw_input("You are in the woods. It looks like early morning or late evening, but you can't really tell. It sounds like there is a stream nearby. You can see smoke coming from somewhere to the left of you and there is a tall tree that looks climbable to your right.")
                                choiceList1 = ["tree", "right", "climb"]
                                if choice in choiceList1:
                                    area = "tree"
                                    choice = raw_input("You climb the tree.\nFrom this height you notice that the smoke appears to be coming from a forest fire in the distance. You see a small clearing that has the relative outline of a stream about 100 yards ahead of you.")
                                    if "down" in choice or "stream" in choice :
                                        area = "start"
                                    else:
                                        choice = raw_input("I don't understand what you mean")
                                elif "stream" in choice:
                                    time = time - 30
                                    choice = raw_input("You go towards the sound of running water.")
                                elif "left" in choice or "smoke" in choice :
                                    time = time - 30
                                    choice = raw_input("You move towards the smoke. After wandering for 30 minutes you notice a very large forest fire moving quickly in your direction. A little ways to your left you see a small concrete building with a heavy iron door.")
                                    if "building" in choice or "left" in choice or "door" in choice:
                                        time = time - 5
                                        choice = raw_input("You move to the building and go inside. You close the door on your way in. There is a small flourescent lamp casting light on a large noticeboard. A paper reads: \"ALL STAFF MUST BE AT SAFE DISTANCE PRIOR TO 1600.\" There is a desk to your right with old office supplies on top of it.")
                                        if "desk" in choice or "supplies" in choice or "office" in choice:
                                            choice = raw_input ("You search the desk and find a wrist watch. It reads " + str(1600 - time))
                                            inv.append("watch")
                                            choice = raw_input()
                                        else:
                                            choice = raw_input("I don't understand what you mean")
                                    else:
                                        choice = raw_input("I don't understand what you mean")
                                else :
                                    choice = raw_input("I don't understand what you mean")
                else:
                    print "You hear an earthshattering boom in the distance and within seconds everything is black.\n\n GAME OVER"
                    quit()