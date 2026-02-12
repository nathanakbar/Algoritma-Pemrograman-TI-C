#penambahan
def my_function(a=5, b=5):
  print(a + b)

my_function()

#pengurangan
def my_function(a=5, b=5):
  print(a - b)

my_function()

#perkalian
def my_function(a=5, b=5):
  print(a * b)

my_function()

#pembagian
def my_function(a=5, b=5):
  print(a / b)

my_function()
 
#modulus
def my_function(a=5, b=5):
  print(a % b)

my_function()

#fibonacci
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 5 Fibonacci numbers
gen = fibonacci()
for _ in range(5):
  print(next(gen))





