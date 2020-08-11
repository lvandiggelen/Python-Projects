#Parent Class Structure
class Structure:
    name= "Pyramid"
    location = "Egypt"
    weather ='hot'

    def getstructureinfo(self):
        entry_method = input("Below or Above")
        number_of_guests = input("Enter number of guests: ")
        entry_password = input("Enter the code: ")
        if (entry_method == self.weather and entry_password == self.location):
            print("Welcome in, {}!".format(entry_method))
        else:
            print("The password is incorrect.")


#Child class Building
class Skyscraper(Structure):
    height = 100
    #height in feet
    location = "NYC"
    size = "10 stories"

    def getstructureinfo(self):
        entry_method = input("Below or Above")
        number_of_guests = input("Enter number of guests: ")
        entry_password = input("Enter the code: ")
        if (entry_method == self.weather and entry_password == self.location):
            print("Welcome in, {}!".format(entry_method))
        else:
            print("The password is incorrect.")


building = Structure()
building.getstructureinfo()

edifice = Skyscraper()
edifice.getstructureinfo()
