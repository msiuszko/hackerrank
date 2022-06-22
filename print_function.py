from xml.dom import xmlbuilder


# drukowanie liczb od 1 do x, w jenej linii bez spacji
import sys

print("Give a number")
x = (int(input()))

for elem in range (1,x+1):
    #print(elem)
    sys.stdout.write(str(elem))