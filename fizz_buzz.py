import time

print("What file would you like to save your results?")
file_out = input("> ")

output = open(file_out, 'a+')

fizz_buzz = "Fizz Buzz"
fizz = "Fizz"
buzz = "Buzz"

start_time = time.time()

for x in range(1, 100):
    if x % 3 == 0 and x % 5 == 0:
        #print(fizz_buzz)
        output.write(str(x) + " " + fizz_buzz + "\n")
    elif x % 3 == 0:
        #print(fizz)
        output.write(str(x) + " " + fizz + "\n")
    elif x % 5 == 0:
        #print(buzz)
        output.write(str(x) + " " + buzz + "\n")
    else:
        #print(x)
        output.write(str(x) + "\n")

print("Program executed in ;", time.time() - start_time)
