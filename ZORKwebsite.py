print "WELCOME TO ZORK 2017"
inv = []
money = 5
name = raw_input("What is your name?")
choiceList1 = []
end = False
choiceTree = []
visited = False
# OBJECTS
vod = True
cloth = True
news = True
while end == False:
    state = False
    while state == False :
            choice = raw_input("Ok, " + name + ", do you prefer the city or the country?")
            if choice == "inv" or choice == "inventory" :
                print inv
                choice = raw_input("")
            if "city" in choice :
                area = "alley"
                inv = [str("$" + str(money)),]
                while area == "alley":
                    choice = raw_input("You wake up in a dark alleyway. There are police sirens in the distance and a shiny object on the ground in a pile of rubbish.")
                    if "object" in choice and vod == True:
                        vod = False
                        choice = raw_input("You pick up the object. It is a large glass bottle with some clear liquid towards the bottom.")
                        inv.append("drink")
                        print "Inventory = |" + str(inv) + "|"
                    if "drink" in choice and "drink" in inv :
                        choice = raw_input("You drink the clear liquid. It has a harsh taste that burns your throat.")
                    else:
                        if "rubbish" in choice :
                            area = "rubbish"
                        while area == "rubbish":
                            if "back" in choice or "alley" in choice or "go back" in choice or "go back to alley" in choice :
                                area = "alley"
                            choice = raw_input("Your look through the rubbish. There are some scraps of cloth and some newspapers.")
                            if "cloth" in choice and cloth == True :
                                cloth = False
                                choice = raw_input("You pick up the cloth and put it in your pocket. It might come in handy later.")
                                inv.append("cloth")
                            elif "newspaper" in choice or "newspapers" in choice and news == True:
                                news = False
                                choice = raw_input("You pick up the newspaper.")
                            inv.append ("newspaper")
                            if "newspaper" in inv and "read" in choice :
                                raw_input("The New York Times, Year 2041.")
                        if area == "rubbish" and cloth == False and news == True :
                            raw_input("There's a few crumpled up newspapers that look slightly usable.")
                        if area == "rubbish" and cloth == True and news == False :
                            raw_input("There's some cloth that still looks usable amongst the trash.")
                        if area == "rubbish" and cloth == False and news == False :
                            raw_input("It's just a pile of trash.")
            else:
                while state == False :
                    if "country" in choice:
                        inv = ["rag", "knife",]
                        choice = raw_input("You are in the woods. It looks like early morning or late evening, but you can't really tell. It sounds like there is a stream nearby. You can see smoke coming from somewhere to the left of you and there is a tall tree that looks climbable to your right.")
                        choiceList1 = ["tree", "right", "climb"]
                        if choice in choiceList1:
                            choice = raw_input("You climb the tree.")
                        elif "stream" in choice:
                            choice = raw_input("You go towards the sound of running water.")
                        else:
                            if "left" or "smoke" in choice :
                                choice = raw_input("You move towards the smoke.")

