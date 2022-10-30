#imports

#variaveis
resp1 = "Weird"
resp2 = "Not Weird"

#head
a = int(input())
par = (a % 2)

if par == 0 and (a >= 2 and a <= 5):
    print(resp2)

elif par == 0 and (a >= 6 and a <= 20):
    print(resp1)

elif par == 0 and a > 20:
    print(resp2)

else:
    print(resp1)