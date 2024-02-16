# Accessing the dictionary items
stu = {
  "name": "Henry",
  "age": "19",
  "grade": 11,
  "place": "NorthBay",
  "hobby": ["Reading","Coding"]

}

# Access the items of a dictionary by referring to its key name, inside square brackets
d = stu["grade"]
print(d)

# There is also a method called get()
g = stu.get("name")
print(g)

# this keys() method will return the keys in the dictionary
k = stu.keys()
print(k)