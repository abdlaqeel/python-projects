from parks import * #import the class created
#Create 3 park objects
p1 = Parks("Big Park", "NL", 200, 1950, 5)
print(p1)
p2 = Parks("Small Park", "ON", 150, 1980, 6)
print(p2)
p3 = Parks("Medium Park", "BC", 165, 1992, 10)
print(p3)

#print their respective day fees
print(p1.getEntryFee(2))
print(p2.getEntryFee(4))
print(p3.getEntryFee(7))

#update the area
print(p1.setArea(400))
#print total park number
print("The total number of Parks is ", Parks.noOfParks)

