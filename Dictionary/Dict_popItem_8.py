# popitem() method removes the last inserted item 
classic = {
    "metal":"Gold",
    "non-metal":"carbon",
    "spices": "Cloves",
    "music": "jaz",
    "juice": "lemon",
    "aircraft":"HAL597"
}

print("Existing items: \n", classic)

# Using popitem() to remove the last inserted item
classic.popitem()
print( "New items: \n" ,classic)