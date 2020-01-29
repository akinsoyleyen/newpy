cities = {
    "Akdeniz": "Mersin", "Mezitli": "Mersin"
}
print(type(cities))
print(cities["Akdeniz"])
print(cities.get("Akdeniz"))

shoes = {"room1": ["nike1","nike2","nike3"], "room2": ["adidas1","adidas2","adidas3"]}

print(shoes["room1"][0])
shoes["room1"] = ["nike4", "nike5", "nike6"]
print(shoes["room1"])