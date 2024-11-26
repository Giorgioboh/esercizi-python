i = 5
k = 0

while i == 5:
    import random
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    k += 1
    if num1 != num2:
        print(num1, num2)

    else:
        print(num1, "=", num2)
        i = 3

print("ci sono voluti" ,k ,"tentativi")
