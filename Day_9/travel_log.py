travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(new_country, new_visits, new_cities):
  # travel_log.append({"country": new_country, "visits": new_visits, "cities": new_cities})
  new_travel = {}
  new_travel["country"] = new_country
  new_travel["visits"] = new_visits
  new_travel["cities"] = new_cities
  travel_log.append(new_travel)
  
  print(f"You have visited {new_country} {new_visits} times.")

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
