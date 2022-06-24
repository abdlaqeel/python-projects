from parks2 import *

s1 = Parks("General Park", "NS", 300, 1963, 5)
print(s1)
print("Cost for 2 days in days in" ,s1.getName(), "is $", "%.2f" % s1.getEntryFee(2)+ "\n")

s2 = ProvincialPark("Big Park", "NL", 200, 1950, 5, 3)
print(s2)

s3 = ProvincialPark("Small Park", "ON", 150, 1980, 4, 2)
print(s3)

s4 = ProvincialPark("Medium Park", "BC", 165, 1992, 3, 3)
print(s4)

s2.setParkRating(1)
print("Park name: ", s2.getName() + "\n" + "Updated rating: ", s2.getParkRating() , "\n")
    
print("Cost for 3 days in days in" ,s2.getName(), "is $", "%.2f" % s2.getEntryFee(3)+ "\n")
print("Cost for 3 days in days in", s3.getName(), "is $","%.2f" % s3.getEntryFee(3)+ "\n")
print("Cost for 3 days in days in", s4.getName(), "is $","%.2f" % s4.getEntryFee(3)+ "\n")

s5= NationalPark("Gros Morne", "NL", 1805, 1973, 6, "Freshwater Fjords")
print(s5)

s6 = NationalPark("Banff", "AB", 6641, 1985, 8, "Lake Louise")
print(s6)

s5.setKnownFor("Tablelands")
print("Park Name: ", s5.getName() + "\n" + "Updates feature: ", s5.getKnownFor() + "\n")

print("Cost for 3 days in days in" ,s5.getName(), "is $", "%.2f" % s5.getEntryFee(3))
print("Cost for 3 days in days in" ,s6.getName(), "is $", "%.2f" % s6.getEntryFee(3))

print("The total number of Parks is: ", Parks.noOfParks)

    
                      
                      
    
