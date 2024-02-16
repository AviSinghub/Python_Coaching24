# The update() method will update the dictionary with the items from the given argument.
sub = {
    "Hindi": "Van ke marg par",
    "Science": "Light and Shadows",
    "Maths": "Algebra",
    "Polity": "The State",
    "Geography": 'Our Earth'
}

print( "Existing lIst: \n ",sub)

# Updatin the existing dictionary list 
sub.update({
  "Polity":"Urban livelihood"
})

print( "Updated  List : \n", sub)