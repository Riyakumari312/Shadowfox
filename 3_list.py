# list of cities in country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# user will give the input(city name)
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# we will check if both countries are in australia
if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")

#  we will check if both countries are in uae
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")

#  we will check if both countries are in india
elif city1 in India and city2 in India:
    print("Both cities are in India")

# If both cities are not in same country 
else:
    print("They don't belong to the same country")