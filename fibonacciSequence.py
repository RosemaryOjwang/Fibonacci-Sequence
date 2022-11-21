n = int(input("Enter a number: "))
def fibonacci(n):
  if n<2:
    return 1
  return (fibonacci(n-1) + fibonacci(n-2))
print("your first " + str(n) +" Fibonacci numbers are:")
for i in range(n):
  print(fibonacci(i), end="\t")
print("\r")


sum = 0
for j in range(n):
  sum += fibonacci(j)
print("sum of the first " + str(n) + " Fibonacci numbers is", sum)