

mySentence = 'I love the color'

color_list = ['red','blue','pink','brown','black']

def color_function(name):
    lst = []
    for i in color_list:
        msg= "{1} {2} {3}".format(name,mySentence,i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name?  ')
        if name == '':
            print("You need to provide your name")
        elif name == "Sally":
            print("Sally can't use this SW")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()
    
