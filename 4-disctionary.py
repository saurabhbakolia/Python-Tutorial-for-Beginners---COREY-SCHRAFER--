disc = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
disc["affordable"] = True
# disc["year"] = 2022
disc.update({"year":2020})
# print(disc.get("D", "NOT FOUND"))
print(disc.keys())
print(disc.values())
print(disc.items())