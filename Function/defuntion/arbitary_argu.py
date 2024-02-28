# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.  
def my_function(*items):
  print("The heaviest fruit " + items[2])

my_function("Grapes", "Apple", "Watermelon", "Figs", "Coconut")  #tuple of arguments