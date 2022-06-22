print("Give a number ")
x = int(input())

if x % 2 == 0 and  x in range (2,5):
    print("Not weird")  
elif x % 2 == 0 and x in range (6,20):
    print("Weird")
elif x % 2 == 0 and x>20:
    print("Not weird")
else:
    print("Weird")
