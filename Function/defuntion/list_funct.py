# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function. 

def my_function(recepie):
  for x in recepie:
    print(x)

fruits = ["Biryani", "Dokla", "Sandwich", "Salad", "chicken tikka", "Butter naan", "Curd rice" ] 

my_function(fruits)