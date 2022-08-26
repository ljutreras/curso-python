a = True
b = False

if a < b :
    print("a < b") 
elif a == b :
    print("a == b")
elif type(a) is bool:
    print("Es booleano")
else:
    print("a > b")

c = 2
d = 1

if c > d or c != d:
    print("Si")

if c > d and c != d:
    print("Si")