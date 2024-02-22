# With the continue statement we can stop the current iteration, and continue with the next:  # Note:5 is missing
j = 0
while j < 10:
  j += 1
  if j == 5:
    continue
  print(j)