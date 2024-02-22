# With the continue statement we can stop the current iteration of the loop, and continue with the next: 

fruits = ["apple", "banana", "cherry","date", "elderberry", "nuts", "peers"]
for x in fruits:
  if x == "date":
    continue
  print(x)