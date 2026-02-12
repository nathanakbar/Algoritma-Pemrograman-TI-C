#functions
def my_function():
  print("Hello")

my_function()

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#scope
def myfunc():
  x = 300
  print(x)

myfunc()

#lambda
x = lambda a : a + 10
print(x(5))

#recursion
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))