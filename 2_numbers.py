#Given values
radius = 84
pi = 3.14
#formula to find area of circle ; Area = pi * radius^2
pond_area = pi * radius**2
print(F"the area of the pond is:,{pond_area: .2f}") #.2f is used to round up to 2 decimal 
#bonus question
water_per_sqmt = 1.4 # given
water_in_pond = pond_area * water_per_sqmt
print(f"Amount of water present in pond:, {water_in_pond: .2f}")
