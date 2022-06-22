#kod1 - drukuje wyniki ale kod jest dwulinijkowy
print("Give the first number")
a = int(input())
print("Give the second number")
b = int(input())
c = a + b
print("The sum of the two numbers are " + str(c))
d = a - b
print("The difference of the two numbers are " + str(d))
e = a * b
print("The contains the product of the two numbers are " + str(e))

#kod2 - drukuje wyniki w jednej linii
print("Give the first and secon number")
a, b = int(input()), int(input())
print((a + b), (a - b), (a * b))


#kod 3 - drukuje wyniki jeden pod drugim
print("Give the first and secon number")
a, b = int(input()), int(input())
print((a + b), (a - b), (a * b), sep='\n')