# Define the city-country mapping
city_to_country = {
    "Sydney": "Australia",
    "Melbourne": "Australia",
    "Brisbane": "Australia",
    "Perth": "Australia",
    "Dubai": "UAE",
    "Abu Dhabi": "UAE",
    "Sharjah": "UAE",
    "Ajman": "UAE",
    "Mumbai": "India",
    "Bangalore": "India",
    "Chennai": "India",
    "Delhi": "India"
}

# Get user input for two cities
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check if both cities are in the mapping
if city1 in city_to_country and city2 in city_to_country:
    # Get the countries of the two cities
    country1 = city_to_country[city1]
    country2 = city_to_country[city2]
    
    # Compare the countries and print the result
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list of known cities")
