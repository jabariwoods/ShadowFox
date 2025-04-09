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

# Get user input for city name
city_name = input("Enter a city name: ")

# Determine and print the country
if city_name in city_to_country:
    country = city_to_country[city_name]
    print(f"{city_name} is in {country}")
else:
    print(f"{city_name} is not in the list of known cities")
