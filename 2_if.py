#list of cities of each country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]

UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

City = input("Enter a city name: ")

# this if -else-elif check which city belongs to which country
if City in Australia:
    print(City, "is in the Australia")
if City in UAE:
    print(City, "is in the UAE")
if City in India:
    print(City, "is in the India")
else:
    print("The given city",City , "doesnot belongs to the list of countries given")