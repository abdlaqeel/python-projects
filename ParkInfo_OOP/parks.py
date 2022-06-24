class Parks: #initialize class var
    __noOfParks = 0 
    def __init__(self, name, loca, area, year, fee):
        self.name = name
        self.loca = loca
        self.area = area
        self.year = year
        self.fee = fee
        type(self).__noOfParks += 1

    def setArea(self, area):
        self.area = area #mutator method for area
        return "Park name: " + self.name + "\n" + "Updated park area: " + str(self.area) + "\n"
        #returns updated area with name
    
    #accesor methods for instance variables
    def getArea(self):
        return self.area
    
    def getName(self):
        return self.name

    def getLoca(self):
        return self.loca

    def getYear(self):
        return self.year

    def getFee(self):
        return self.fee 

    #calculates entry fees
    def getEntryFee(self, days):
        entryFee = days * self.fee
        entryFee = "%.2f" % entryFee #formats in format required
        return "Cost for " + str(days) + " days in " + self.name + " is $ " + str(entryFee) + "\n"

    def getnoOfParks():
        return "The total number of Parks is " + noOfParks
    
    def ParkNum(self, __noOfParks):
        return __noOfParks
    
    def __str__(self):
        return "Park name: " + self.name + "\n" + "Location: " + str(self.loca) + "\n" + "Area covered (km^2): " + str(self.area) + "\n" + "Year established: " + str(self.year)+ "\n" + "Entry fee per day: $" + str(self.fee) + "\n"      
        #returns output in string and moves to nextr line for each variable
