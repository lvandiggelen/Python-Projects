



def start(nice = 0, mean=0, name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,nice)

def describe_game(name):
    if name!= ":
    print("\nThank you for playing again, {}!".format(name))
    else:
        stop= True
        while stop:
            if name== "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name !="":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people.\nYou may choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name
                

    




if __name__=="__main__":
    start()
