# Question 1
def greet():
  print("Hello, World!")
    
greet()

# Question 2 
def personalized_greeting(name):
  print("Hello, " + name + "!")

personalized_greeting("Keyat")

# Question 3
def square(number):
  return number * number

print(square(5))

# Question 4 
def rectangle_area(length, width):
  return length + width 

print(rectangle_area(4,5))

# Question 5
def apply_operation(function, number):
  return function(number)
def double(number):
  return number * 2

print(apply_operation(double, 7))
print(apply_operation(square, 3))
