# pop() method removes the item from the specific key name.
daily = {
    "metal":"Aluminium",
    "non-metal":"oxygen",
    "cotton": "shirt",
    "plastic": "bottle",
    "wood": "tree",
    "cement":"building"
}
# existing items
print("Existing items: \n", daily)

# use pop() to remove the key 
daily.pop("plastic")
print( "New items: \n", daily)