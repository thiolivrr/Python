def location(city, country, population=0):
    if population != 0:
        place = (f"{city.capitalize()}, {country.capitalize()} - population {population}")
    else:
        place = (f"{city.capitalize()}, {country.capitalize()}")
    
    return place